from reviews_service.init import app
from reviews_service.users import get_user_service


def initialize():
    services_ = (get_user_service(),)
    for service in services_:
        service.init()


if __name__ == '__main__':
    initialize()
    app.run()
