from tkinter.messagebox import NO
from django.views import View
from django.core.cache import cache
from .utils.Request import Request
from django.http import JsonResponse


request = Request()


class APIviews(View):
    """methodos de la aplicacion"""

    def get(self, req, idx=None, n_max=None):
        """endpoint que recibe un indice i, un numero
        máximo de hisotrias n y devuelve los
        detalles de las n hisotiras"""
        if cache.get('full_lst'):
            return JsonResponse(request.req(idx, n_max), safe=False)
        if idx is None or n_max is None:
            request.store_result()
            idx = 1
            n_max = 1
        if idx > 500 or n_max > 500:
            return JsonResponse('Out of index', safe=False)
        lst = request.req_one(idx, n_max)
        cache.set('lst', lst, 10)
        return JsonResponse(lst, safe=False)

    def delete(self):
        """delete cache"""
        cache.delete('full_lst')
        return JsonResponse('Cache deleted succesfull', safe=False)
