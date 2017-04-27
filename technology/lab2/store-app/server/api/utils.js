/**
 * Created by Drapegnik on 4/25/17.
 */

import HttpError from 'node-http-error';

export const checkIsFound = (object) => {
  if (!object) {
    throw (new HttpError(404));
  }

  return object;
};

export const checkIdCast = (id, castFunc) => {
  let castedId;

  try {
    castedId = castFunc(id);
  } catch (err) {
    throw (new HttpError(404));
  }

  if (!castedId) {
    throw (new HttpError(404));
  }

  return castedId;
};
