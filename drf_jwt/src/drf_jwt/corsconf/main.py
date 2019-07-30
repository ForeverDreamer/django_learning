from corsheaders.defaults import default_headers


CORS_URLS_REGEX = r'^/api/.*$'  # CORS HEADERS ENABALED

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1',
)

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)

