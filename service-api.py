import os
from service import app, config
from service.admin import init_admin

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if config('DEBUG', default=False, cast=bool):
        init_admin()
    app.run(host='0.0.0.0', port=port)

