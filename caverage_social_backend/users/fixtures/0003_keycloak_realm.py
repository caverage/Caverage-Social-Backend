from dynamic_fixtures.fixtures import BaseFixture

from django_keycloak.models import Realm, Server


class Fixture(BaseFixture):

    dependencies = (("users", "0002_keycloak_server"),)

    def load(self):
        server = Server.objects.get(url="https://auth.cavera.ge")

        Realm.objects.get_or_create(
            server=server, name="master",
        )
