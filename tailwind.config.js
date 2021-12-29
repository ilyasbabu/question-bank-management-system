module.exports = {
  content: [
    './layouts/*.html'
  ],
  theme: {
    extend: {
      
    },
  },
  plugins: [
    require("@tailwindcss/forms")({
      strategy: 'class',
    }),
  ],
}
