import rawRules from './rules.json';
import attributes from './attributes.json';

const rules = rawRules.map((rule, i) => ({ ...rule, id: i + 1 }));

export { attributes, rules };
