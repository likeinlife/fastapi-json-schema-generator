class MockAppSettings:
    name = "TestAPI"
    version = "0"
    debug = True


class MockDBSettings:
    password = "postgres"
    user = "postgres"
    host = "postgres"
    port = "postgres"
    db_name = "postgres"

    def get_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}: {self.password}@{self.host}:{self.port}/{self.db_name}"


class MockLoggingSettings:
    level = "DEBUG"
    json_format = False


class MockSettings:
    app = MockAppSettings()
    db = MockDBSettings()
    log = MockLoggingSettings()
