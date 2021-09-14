const colors = require('tailwindcss/colors');

module.exports = {
  purge: {
    enabled: false,
    content: [
      './src/html/**/*.{html}',
      './src/css/**/*.{css}',
      './src/js/**/*.{js,jsx}'
    ]
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'bluegray': colors.blueGray,
        'coolgray': colors.coolGray,
        'gray': colors.gray,
        'truegray': colors.trueGray,
        'warmgray': colors.warmGray,
        'red': colors.red,
        'orange': colors.orange,
        'amber': colors.amber,
        'yellow': colors.yellow,
        'lime': colors.lime,
        'green': colors.green,
        'emerald': colors.emerald,
        'teal': colors.teal,
        'cyan': colors.cyan,
        'sky': colors.sky,
        'blue': colors.blue,
        'indigo': colors.indigo,
        'violet': colors.violet,
        'purple': colors.purple,
        'fuchsia': colors.fuchsia,
        'pink': colors.pink,
        'rose': colors.rose
      },
      fontFamily: {
        'sans': ['Inter', '"M PLUS 1p"', 'Meiryo', 'sans-serif'],
        'icon': ['Material Icons'],
        'weather-icon': ['WeatherIcons']
      },
      spacing: {
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        '1/12': '8.333333%',
        '2/12': '16.666667%',
        '3/12': '25%',
        '4/12': '33.333333%',
        '5/12': '41.666667%',
        '6/12': '50%',
        '7/12': '58.333333%',
        '8/12': '66.666667%',
        '9/12': '75%',
        '10/12': '83.333333%',
        '11/12': '91.666667%',
        '7/24': '29.166667%',
        '18': '4.5rem',
        '68': '17rem',
        '112': '28rem',
        '128': '32rem',
        '144': '36rem',
        '360': '22.5rem',
        '640': '40rem',
        '768': '48rem',
        '915': '57.1875rem',
        '1024': '64rem',
        '1920': '120rem'
      },
      borderRadius: {
        '4xl': '2rem',
        '5xl': '2.5rem',
        '6xl': '3rem',
        '7xl': '3.5rem',
        '8xl': '4rem'
      }
    }
  },
  variants: {
    extend: {}
  },
  plugins: []
};
