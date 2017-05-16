/**
 * Created by Drapegnik on 23.03.17.
 */
package app.backend;

import app.config.Options;
import app.models.Mark;
import app.models.Student;
import app.models.Subject;
import app.models.wrappers.Students;
import org.xml.sax.SAXException;

import javax.xml.XMLConstants;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamReader;
import javax.xml.transform.stax.StAXSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;
import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class xmlDriver extends dbDriver {
    /**
     * Get all {@link Student}'s objects from storage
     *
     * @return <pre>{@code List<Student>}</pre> {@link Student}'s objects
     */
    @Override
    public List<Student> getStudents() {
        System.out.println("Select students...");
        ArrayList<Student> data = readData(getStudentsFilename());
        System.out.println("Successfully select " + data.size() + " students.");
        return data;
    }

    /**
     * Get all {@link Student}'s objects from storage
     * that have 3 and more bad (1, 2, 3) marks
     *
     * @return <pre>{@code List<String>} students_ids</pre>
     */
    @Override
    public List<String> getBadStudentsIds() {
        System.out.println("Select bad students...");
        ArrayList<String> badIds = new ArrayList<>();
        ArrayList<Student> data = readData(getStudentsFilename());

        for (Student st : data) {
            int badMarksCount = 0;
            for (Mark mr : st.getMarks()) {
                if (mr.getGrade() < 4) {badMarksCount++;}
            }

            if (badMarksCount > 2) {
                badIds.add(st.getId());
                System.out.println(st.getId());
            }
        }

        System.out.println("Successfully select " + badIds.size() + " bad students.");
        return badIds;
    }

    /**
     * Delete {@link Student} and all his {@link Mark}s from storage
     *
     * @param id {@link Student#id}
     */
    @Override
    public void deleteStudent(String id) {
        System.out.println("Delete student...");
        ArrayList<Student> data = readData(getStudentsFilename());
        int ind = -1;

        for (int i = 0; i < data.size(); i++) {
            if (data.get(i).getId().equals(id)) {
                ind = i;
                break;
            }
        }

        if (ind == -1) {return;}

        data.remove(ind);
        writeData(data);
        System.out.println("Successfully delete student with id=" + id);
    }

    /**
     * Create and save {@link Student} object in storage
     *
     * @param student {@link Student} instance
     */
    @Override
    public void createStudent(Student student) {
        ArrayList<Student> data = readData(getStudentsFilename());
        data.add(student);
        writeData(data);
    }

    /**
     * Create {@link Mark} object in storage
     *
     * @param mark {@link Mark} instance
     */
    @Override
    public void createMark(Mark mark) {
        ArrayList<Student> data = readData(getStudentsFilename());
        boolean found = false;

        for (Student st : data) {
            if (st.getId().equals(mark.getStudentId())) {
                st.addMark(mark);
                found = true;
                break;
            }
        }

        if (!found) {return;}

        writeData(data);
    }

    /**
     * Fetch {@link Student}s data from {@link Options#STUDENTS_FILE_NAME}
     * Generate random {@link Mark}s with {@link Subject}s
     * Save all data into xml-file
     *
     * @see xmlDriver#writeData(ArrayList)
     * @see Options#STUDENTS_FILE_NAME
     */
    private void initStorage() {
        System.out.println("Init storage...");
        ArrayList<Student> data = Student.readFromFile(Options.STUDENTS_FILE_NAME);
        Random random = new Random();

        for (Student student : data) {
            ArrayList<Mark> marks = new ArrayList<>();
            for (Subject subject : Subject.values()) {
                marks.add(new Mark(subject, random.nextInt(10) + 1, student.getId()));
            }
            student.setMarks(marks);
        }

        writeData(data);
    }

    private void writeData(ArrayList<Student> data) {
        try {
            File file = new File(getStudentsFilename());
            JAXBContext jaxbContext = JAXBContext.newInstance(Students.class);
            Marshaller jaxbMarshaller = jaxbContext.createMarshaller();
            jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
            jaxbMarshaller.marshal(new Students(data), file);
        } catch (JAXBException e) {
            e.printStackTrace();
        }
    }

    private ArrayList<Student> readData(String filename) {
        ArrayList<Student> data = new ArrayList<>();
        try {
            XMLStreamReader reader = XMLInputFactory.newInstance().createXMLStreamReader(new FileInputStream(filename));
            SchemaFactory sf = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
            String xcdFileName = filename.substring(0, filename.length() - 3) + "xsd";
            System.out.println(xcdFileName);
            Schema schema = sf.newSchema(new File(xcdFileName));
            Validator validator = schema.newValidator();
            validator.validate(new StAXSource(reader));

            System.out.println("Document is valid");
            JAXBContext jaxbContext = JAXBContext.newInstance(Students.class);

            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            Students students = (Students) jaxbUnmarshaller.unmarshal(new File(filename));
            for (Student st : students.getData()) {
                data.add(st);
            }
        } catch (SAXException e) {
            System.err.println("Document is invalid!!");
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return data;
    }

    private static String getStudentsFilename() {
        return Options.XML_DIR + Student.class.getSimpleName() + "s.xml";
    }

    public static void main(String[] args) {
        xmlDriver xml = new xmlDriver();
        // Student.writeInFile(app.config.Options.STUDENTS_FILE_NAME, Student.generateFakeData());
        xml.initStorage();
        xml.readData(getStudentsFilename());
    }
}
