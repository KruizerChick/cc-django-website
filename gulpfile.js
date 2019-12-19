////////////////////////////////
// Setup
////////////////////////////////

// Gulp and package
const { src, dest, parallel, series, watch } = require('gulp')
const pjson = require('./package.json')

// Plugins
const autoprefixer = require('autoprefixer')
const browserSync = require('browser-sync').create()

const cssnano = require ('cssnano')
const imagemin = require('gulp-imagemin')
const pixrem = require('pixrem')
const plumber = require('gulp-plumber')
const postcss = require('gulp-postcss')
const reload = browserSync.reload
const rename = require('gulp-rename')
const sass = require('gulp-sass')
const spawn = require('child_process').spawn
const uglify = require('gulp-uglify-es').default

////////////////////////////////
// Paths
////////////////////////////////

function pathsConfig(appName) {
  this.app = `./${pjson.name}`

  // Make sure this path points to the correct node_modules directory
  const vendorsRoot = './node_modules'

  return {
    
    app: this.app,
    templates: `${this.app}/templates`,
    sass: `${this.app}/assets/sass`,
    assets: {
      css: `${this.app}/assets/css`,
      js: `${this.app}/assets/js`,
      images: `${this.app}/assets/images`
    },
    static: {
      css: `./static/css`,
      js: `./static/js`,
      fonts: `./static/fonts`,
      images: `./static/images`,
    },
  }
}

var paths = pathsConfig()

////////////////////////////////
// Tasks
////////////////////////////////

// Styles autoprefixing and minification
function styleProject() {
  var processCss = [
      autoprefixer(), // adds vendor prefixes
      pixrem(),       // add fallbacks for rem units
  ]

  var minifyCss = [
      cssnano({ preset: 'default' })   // minify result
  ]

  return src(`${paths.sass}/project.scss`)
    .pipe(sass({
      includePaths: [
        paths.sass
      ]
    }).on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(postcss(processCss))
    .pipe(dest(paths.static.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(postcss(minifyCss)) // Minifies the result
    .pipe(dest(paths.static.css))
}

function styleAdmin() {
  var processCss = [
      autoprefixer(), // adds vendor prefixes
      pixrem(),       // add fallbacks for rem units
  ]

  var minifyCss = [
      cssnano({ preset: 'default' })   // minify result
  ]

  return src(`${paths.sass}/admin.scss`)
    .pipe(sass({
      includePaths: [
        
        paths.sass
      ]
    }).on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(postcss(processCss))
    .pipe(dest(paths.static.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(postcss(minifyCss)) // Minifies the result
    .pipe(dest(paths.static.css))
}

// Run both project and admin style processes
const styles = parallel(styleAdmin, styleProject);

// Javascript minification
function scripts() {
  return src(`${paths.assets.js}/project.js`)
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.static.js))
}

// Image compression
function imgCompression() {
  return src(`${paths.assets.images}/**/*`)
    .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
    .pipe(dest(paths.static.images))
}

// Run django server
function runServer(cb) {
  var cmd = spawn('python', ['manage.py', 'runserver', '--settings=config.settings.local'], {stdio: 'inherit'})
  cmd.on('close', function(code) {
    console.log('runServer exited with code ' + code)
    cb(code)
  })
}

// Browser sync server for live reload
function initBrowserSync() {
  browserSync.init(
    [
      `${paths.static.css}/*.css`,
      `${paths.static.js}/*.js`,
      `${paths.templates}/*.html`
    ], {
      // https://www.browsersync.io/docs/options/#option-proxy
      proxy: 'localhost:8000'
      
    }
  )
}

// Watch
function watchPaths() {
  watch(`${paths.sass}/modules/_admin.scss`, styleAdmin),
  watch(`${paths.sass}/**/*.scss`, styleProject),
  watch(`${paths.assets.images}/**/*`, imgCompression),
  watch(`${paths.templates}/**/*.html`).on("change", reload)
  watch([`${paths.assets.js}/*.js`, `!${paths.assets.js}/*.min.js`], scripts).on("change", reload)
}

// Generate all assets
const generateAssets = parallel(
  styles,
  scripts,
  imgCompression
)

// Set up dev environment
const dev = parallel(
  runServer,
  initBrowserSync,
  watchPaths
)

exports.default = series(generateAssets, dev)
exports["generate-assets"] = generateAssets
exports["dev"] = dev
