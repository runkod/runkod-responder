PATH_SEPARATOR = '/'
DIR_INDEX = 'index.html'
DIR_INDEX_SEARCH_TRY = 6

PROJECT_STATUS_ON = 1
PROJECT_STATUS_MAINTENANCE = 2
PROJECT_STATUS_OFF = 3

MB = 1024 * 1024

# this will change when gaia support gzip encoding
FILE_SERVE_RULES = {
    'html': MB * 2,
    'css': MB * 4,
    'js': MB * 10
}
