from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Users, Account, Transfers, Store
from  .serializers import UsersSerializer, AccountSerializer, TransferSerializer, StoreSerializer

class UsersView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users,many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        users = request.data.get('users')
        serializer = UsersSerializer(data=users)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.name)})

    def put(self, request, pk):
        saved_user = get_object_or_404(Users.objects.all(), pk=pk)
        data = request.data.get('users')
        serializer = UsersSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({
            "success": "User '{}' updated successfully".format(user_saved.name)
        })

    def delete(self, request, pk):
        user = get_object_or_404(Users.objects.all(), pk=pk)
        user.delete()
        return Response({
            "message": "User with id `{}` has been deleted.".format(pk)
        }, status=204)

class AccountsView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts,many=True)
        return Response({"accounts": serializer.data})

    def post(self, request):
        accounts = request.data.get('accounts')
        serializer = AccountSerializer(data=accounts)
        if serializer.is_valid(raise_exception=True):
            account_saved = serializer.save()
        return Response({"success": "Account '{}' created successfully".format(account_saved.id)})

    def put(self, request, pk):
        saved_account = get_object_or_404(Account.objects.all(), pk=pk)
        data = request.data.get('accounts')
        serializer = AccountSerializer(instance=saved_account, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            account_saved = serializer.save()
        return Response({
            "success": "Account '{}' updated successfully".format(account_saved.id)
        })

    def delete(self, request, pk):
        account = get_object_or_404(Account.objects.all(), pk=pk)
        account.delete()
        return Response({
            "message": "Account with id `{}` has been deleted.".format(pk)
        }, status=204)

class TransfersView(APIView):
    def get(self, request):
        transfers = Transfers.objects.all()
        serializer = TransferSerializer(transfers,many=True)
        return Response({"transfers": serializer.data})

    def post(self, request):
        transfers = request.data.get('transfers')
        serializer = TransferSerializer(data=transfers)
        if serializer.is_valid(raise_exception=True):
            transfer_saved = serializer.save()
        return Response({"success": "Transfers '{}' created successfully".format(transfer_saved.id)})

    def put(self, request, pk):
        saved_transfer = get_object_or_404(Transfers.objects.all(), pk=pk)
        data = request.data.get('transfers')
        serializer = TransferSerializer(instance=saved_transfer, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            transfer_saved = serializer.save()
        return Response({
            "success": "Transfers '{}' updated successfully".format(transfer_saved.id)
        })

    def delete(self, request, pk):
        account = get_object_or_404(Transfers.objects.all(), pk=pk)
        account.delete()
        return Response({
            "message": "Transfers with id `{}` has been deleted.".format(pk)
        }, status=204)

class StoreView(APIView):
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store,many=True)
        return Response({"store": serializer.data})

    def post(self, request):
        store = request.data.get('store')
        serializer = StoreSerializer(data=store)
        if serializer.is_valid(raise_exception=True):
            store_saved = serializer.save()
        return Response({"success": "Store '{}' created successfully".format(store_saved.id)})

    def put(self, request, pk):
        saved_store = get_object_or_404(Store.objects.all(), pk=pk)
        data = request.data.get('store')
        serializer = StoreSerializer(instance=saved_store, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            store_saved = serializer.save()
        return Response({
            "success": "Store '{}' updated successfully".format(store_saved.id)
        })

    def delete(self, request, pk):
        store = get_object_or_404(Store.objects.all(), pk=pk)
        store.delete()
        return Response({
            "message": "Store with id `{}` has been deleted.".format(pk)
        }, status=204)

