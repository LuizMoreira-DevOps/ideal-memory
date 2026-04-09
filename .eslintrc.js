// GUIA ESLINT: https://eslint.org/docs/latest/use/configure/migration-guide
// .eslintrc.js

module.exports = {
  // ...other config
  plugins: ["jsdoc"],
  rules: {
    "jsdoc/require-description": "error",
    "jsdoc/check-values": "error",
  },
  // ...other config
};
