class NoCodeLowCodeBuilder:
    def __init__(self):
        self.applications = []

    def create_application(self, name, description):
        app = {
            'name': name,
            'description': description,
            'components': []
        }
        self.applications.append(app)
        return app

    def add_component(self, app_name, component):
        for app in self.applications:
            if app['name'] == app_name:
                app['components'].append(component)
                return app
        return None

    def list_applications(self):
        return self.applications

    def export_application(self, app_name):
        for app in self.applications:
            if app['name'] == app_name:
                return f"Exporting application: {app}"
        return None

# Example Usage
if __name__ == "__main__":
    builder = NoCodeLowCodeBuilder()
    app1 = builder.create_application("My First App", "This is a no-code application")
    builder.add_component("My First App", {"type": "button", "label": "Click Me"})
    print(builder.list_applications())
    print(builder.export_application("My First App"))