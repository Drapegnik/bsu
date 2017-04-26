/**
 * Created by Drapegnik on 26.03.17.
 */

export default function (req, res, next) {
  if (!req.user) {
    return res.sendStatus(401);
  }

  return next();
}
