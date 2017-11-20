import rawRules from './rules';
import attributes from './attributes';

const rules = rawRules.map((rule, i) => ({ ...rule, id: i + 1 }));

export { attributes, rules };
