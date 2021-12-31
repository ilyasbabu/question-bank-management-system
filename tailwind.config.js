module.exports = {
  purge: {
    content: ['./src/**/*.html'],
    safelist: [
      'bg-slate-700',
      'shadow-lg',
      'p-4',
      'text-white',
    ]
  },
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
