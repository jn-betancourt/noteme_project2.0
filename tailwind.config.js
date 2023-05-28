/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
      'nav-color': "#6366F1",
      'dark': "#1E293B",
      'grey': "#B8BFC6",
      'light': "#FFFFFF"
    }
  },
  },
  plugins: [],
}