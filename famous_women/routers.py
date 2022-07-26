from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}{trailing_slash}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}{trailing_slash}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=False,
                      initkwargs={'suffix': 'Detail'})
    ]
