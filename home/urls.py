from django.urls import path

from home.appviews.index_page import Index
from home.appviews.about_page import About
from home.appviews.contact_page import Contact
from home.appviews.upload_data import UploadData
from home.appviews.search import Search
from home.appviews.products import Products
from home.appviews.product_detail import ProductDetail
from home.appviews.categories import Category
from home.appviews.cart import Cart
from home.appviews.update_cart import UpdateCart
from home.appviews.update_cartpage import UpdateCartPage
from home.appviews.remove_cart_item import RemoveCartItem
from home.appviews.checkout import Checkout
from home.appviews.product_orders import ProductOrders
from home.appviews.delete_order import DeleteOrder
from home.appviews.user_signup import UserSignup
from home.appviews.user_login import UserLogin
from home.appviews.user_logout import UserLogout
from home.appviews.add_product import AddProduct
from home.appviews.edit_product import EditProduct
from home.appviews.update_product import UpdateProduct
from home.appviews.delete_product import DeleteProduct
from home.appviews.hide_show_product import HideShowProduct

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about',  About.as_view(), name='about'),
    path('contact',  Contact.as_view(), name='contact'),
    path('uploadfile', UploadData.as_view(), name='uploadfile'),
    path('search', Search.as_view(), name="search"),

    path('products/<str:filter>', Products.as_view(), name='products'),
    path('productdetail/<str:retailer_sku>', ProductDetail.as_view(), name='productdetail'),
    path('categories/<str:category>', Category.as_view(), name='category'),

    path('cart', Cart.as_view(), name='cart'),
    path('update_cart/<str:retailer_sku>/<str:availability>', UpdateCart.as_view(), name='updatecart'),
    path('update_cartpage', UpdateCartPage.as_view(), name='updatecart'),
    path('remove_item/<str:retailer_sku>', RemoveCartItem.as_view(), name='remove_item'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', ProductOrders.as_view(), name='orders'),
    path('delete_order/<str:id>', DeleteOrder.as_view(), name="delete_order"),

    path('signup', UserSignup.as_view(), name="handle_signUp"),
    path('login', UserLogin.as_view(), name="handle_login"),
    path('logout', UserLogout.as_view(), name="handle_logout"),

    path('add/<str:filter>', AddProduct.as_view(), name="add"),
    path('edit', EditProduct.as_view(), name="edit"),
    path('update/<str:retailer_sku>/<str:filter>', UpdateProduct.as_view(), name="update"),
    path('delete/<str:retailer_sku>/<str:filter>', DeleteProduct.as_view(), name="delete"),

    path('hide_product/<str:retailer_sku>/<str:filter>', HideShowProduct.as_view(), name="hide_product"),
]
