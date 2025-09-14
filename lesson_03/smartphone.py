class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def get_brand_name(self):
        return self.brand

    def get_model_name(self):
        return self.model

    def get_number(self):
        return self.number
