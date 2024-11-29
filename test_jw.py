import model
import view
import controller

if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model, view)
    