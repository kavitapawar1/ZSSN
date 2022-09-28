
from django.http import JsonResponse, HttpResponseBadRequest
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Survivor
from .serializers import SurvivorSerializer


class Survivors(APIView):
    def get(self, request):
        survivors = Survivor.objects.all()
        serializer = SurvivorSerializer(survivors, many=True).data
        return JsonResponse(serializer, safe=False)

    def post(self, request):    
        try :
            name = request.data.get("name", None)
            age =  request.data.get("age", None)
            gender = request.data.get('gender', None)
            latitude = request.data.get('latitude', None)
            longitude = request.data.get('longitude', None)
            is_infected = request.data.get('is_infected', None)
            
            survivor = Survivor.objects.create(
                name = name,
                age =  age,
                gender = gender,
                latitude = latitude,
                longitude = longitude,
                is_infected = is_infected,   
            )
            
            survivor_data= SurvivorSerializer(survivor).data
            return JsonResponse(survivor_data)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({"error":e}), content_type="application/json", status=404)
    

class ServivorById(APIView):
    def get(self, request, id):
        try:
            survivor = Survivor.objects.get(id=id)
            survivor_data= SurvivorSerializer(survivor).data
            return JsonResponse(survivor_data)
        except Survivor.DoesNotExist:
            return HttpResponseBadRequest(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)
    
    def put(self, request, id):  
        try:
            try :
                survivor = Survivor.objects.get(id=id)
            except Survivor.DoesNotExist:
                return HttpResponseBadRequest(json.dumps({"error":"Survivor does not exists"}), content_type="application/json", status=404)
            
            latitude = request.data.get('latitude', None)
            longitude = request.data.get('longitude', None)
            is_infected = request.data.get('is_infected', None)
            
            survivor.latitude = latitude
            survivor.longitude = longitude
            survivor.is_infected = is_infected
            survivor.save()
            
            survivor_data= SurvivorSerializer(survivor).data
            return JsonResponse(survivor_data)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({"error":e}), content_type="application/json", status=404)
        
            
class InfectedRecords(APIView):
    def get(self, request):
        infected_survivor = 0.0

        survivors = Survivor.objects.all()
        for survivor in survivors:
            if survivor.is_infected == True:
                infected_survivor += 1

        total_survivor = survivors.count()
        percentage = ( infected_survivor / total_survivor )*100
        return JsonResponse(json.dumps({"Percentage of infected survivors": percentage}), content_type="application/json", status=200, safe=False)


class NonInfectedRecords(APIView):
    def get(self, request):
        non_infected_survivor = 0.0

        survivors = Survivor.objects.all()
        for survivor in survivors:
            if survivor.is_infected != True:
                non_infected_survivor += 1

        total_survivor = survivors.count()
        percentage = ( non_infected_survivor / total_survivor )*100
        return JsonResponse(json.dumps({"Percentage of non infected survivors": percentage}), content_type="application/json", status=200, safe=False)

            
        
        
