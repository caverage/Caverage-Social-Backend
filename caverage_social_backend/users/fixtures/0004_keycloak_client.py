from dynamic_fixtures.fixtures import BaseFixture

from django_keycloak.models import Realm, Client


class Fixture(BaseFixture):

    dependencies = (("users", "0003_keycloak_realm"),)

    def load(self):
        realm = Realm.objects.get(name="master")

        Client.objects.get_or_create(realm=realm, client_id="social", secret="")

