from rest_framework.response import Response
from .serializers import HeroSerializer
from .models import Hero
from rest_framework.views import APIView


class HeroDetails(APIView):
    def get(self,request):
        try:
            heroes=Hero.objects.all()
            serializer = HeroSerializer(heroes, many=True)
            return Response({"data":serializer.data,"message":"Successfully Done"},status=200)
        except:
            return Response({"message": "Heros not found"}, status=404)
        

class HeroDetail(APIView):
    def get(self,request,hero_id):
        try:
            hero=Hero.objects.get(id=hero_id)
            serializer = HeroSerializer(hero)
            return Response({"data":serializer.data,"message":"Successfully Done"},status=200)
        except:
            return Response({"message": "Hero not found"}, status=404)
        

class AddHero(APIView):
    def post(self,request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new hero object to the database
            serializer.save()
            return Response({"message": "Hero added successfully"}, status=200)
        else:
            return Response(serializer.errors, status=503)



class DeleteHero(APIView):
    def delete(self,request,hero_id):
        try:
            hero = Hero.objects.get(id=hero_id)
            hero.delete()
            return Response({"message": "Hero removed successfully"}, status=200)
        except :
            return Response({"message": "Hero not found"}, status=200)



class DeleteHeroes(APIView):
    def delete(self,request):
        try:
            heroes = Hero.objects.all()
            heroes.delete()
            return Response({"message": "Heroes removed successfully"}, status=200)
        except :
            return Response({"message": "Something went wrong"}, status=503 )
        

class UpdateHero(APIView):
    def put(self,request,hero_id):
        try:
            hero=Hero.objects.get(id=hero_id)
            serializer=HeroSerializer(hero,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({"data":serializer.data,"message":"Update hero successfully"},status=200)
            else:
                 return Response({"message":"not updated"},status=503)
        except:
             return Response({"message": "Hero not found"}, status=200 )


