import { rules as initialRules } from 'data';
import { attributes } from 'data';

export const mainTarget = 'club';

export default class {
  constructor(getContext, updateContext, askQuestion, finish, log) {
    this.getContext = getContext;
    this.updateContext = updateContext;
    this.askQuestion = askQuestion;
    this.finish = finish;
    this.log = log;
  }

  async start() {
    const targets = [mainTarget];
    let rules = [...initialRules];

    while (true) {
      const currentTarget = targets[targets.length - 1];
      const currentRule = rules.find(({ then: { attr } }) => attr === currentTarget);

      if (!currentRule) {
        const target = targets.pop();
        if (target === mainTarget) {
          break;
        }

        console.log(`> ask about ${target}`);
        const options = attributes.find(({ name }) => name === target).values;
        const answer = await this.askQuestion(target, options);

        console.log('> answer: ', answer);
        this.updateContext(target, answer);
        continue;
      }

      const result = this.checkRule(currentRule.if);
      if (result === true) {
        const target = targets.pop();
        const { value } = currentRule.then;

        console.log(`> find ${target}=${value}`);
        this.log(currentRule);

        this.updateContext(target, value);
        if (!targets.length) {
          break;
        }
        rules = rules.filter(({ id }) => id !== currentRule.id);
      } else if (result !== false) {
        targets.push(result);
        console.log('> targets: ', targets);
        continue;
      }
      rules = rules.filter(({ id }) => id !== currentRule.id);
    }
    this.finish();
  }

  checkRule(conditions) {
    const context = this.getContext();
    for (let condition of conditions) {
      const { attr, value } = condition;

      if (!context.hasOwnProperty(attr)) {
        return attr;
      }

      if (context[attr] !== value) {
        return false;
      }
    }
    return true;
  }
}
