
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"]={}
        self.carrito=carrito

    def agregar(self, producto):
        if producto.idprod not in self.carrito.keys():
            self.carrito[producto.idprod]={
                "idprod":producto.idprod,
                "nombreproduc":producto.nombreproduc,
                "descripcion":producto.descripcion,
                "precio":str(producto.precio),
                "stock":1,
                "total": producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==producto.idprod:
                    value["stock"]= value["stock"]+1
                    value["precio"]= producto.precio
                    value["total"]=  value["total"]+producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, producto):
        id = producto.idprod
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar (self, producto):
        for key, value in self.carrito.items():
            if key == producto.idprod:
                value["stock"]= value["stock"]-1
                value["total"] = int(value["total"])- producto.precio
                if value["stock"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 