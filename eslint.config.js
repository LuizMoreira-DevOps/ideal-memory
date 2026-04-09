// GUIA ESLINT: https://eslint.org/docs/latest/use/configure/migration-guide
// eslint.config.js

export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: "script",
      globals: {
        document: "readonly",
        window: "readonly",
        console: "readonly",
        alert: "readonly",
      },
    },
    rules: {
      semi: ["error", "always"],
      "no-unused-vars": "warn",
    },
  },
];
