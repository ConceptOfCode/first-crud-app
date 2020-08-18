from django.urls import path
from django.urls import include
from crud_application.Views import EquipmentsView

urlpatterns = [
    # path('', homeView.index, name="indexPage"),
    # path('addPage', homeView.addPage, name="addPage"),
    # path('add/branch', homeView.addBranches, name="renderAddBranches"),
    # path('insert/Branch', homeView.insertBranch, name='doAddBranch'),
    # path('postAddPage', homeView.addPagePost, name="addPagePost"),
    # path('update/updateInfo/<int:id>', homeView.updatePage, name='updateInformations'),
    # path('update/info', homeView.updatePagePost, name='doUpdate'),
    # path('delete/<int:id>', homeView.delete, name="doDelete"),
    path('', EquipmentsView.index, name='index'),
    path('add/Equip', EquipmentsView.renderEquAdd, name='equAdd'),
    path('add/equipmentsNew', EquipmentsView.addEqu, name='addNewEqu'),
    path('update/Equipment/<equID>', EquipmentsView.renderUpdate, name='update'),
    path('update/doUpdate', EquipmentsView.update, name='updating'),
    path('delete/Equipment/<equID>', EquipmentsView.delete, name='delete'),
    path('test/getResponse', EquipmentsView.retriveDataTest),
]