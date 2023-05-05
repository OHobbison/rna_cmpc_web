from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import Contact,Id_hub
from .forms import NewUserForm,UploadCSVForm
from .utils import get_graph,generate_scatter_plot
import csv,io
from django.contrib.auth import login, authenticate,logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import pandas as pd
import json
import numpy as np
import re 


# Create your views here
@login_required(login_url='user-login')
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

@login_required(login_url='user-login')
def aplicar_rna(request):
    context = {}
    return render(request,'base/aplicar_rna.html',context)


def userLogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})

def userRegister(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})

def userLogout(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

#Upload CSV

def show_ids(request):
	template = 'base/aplicar_rna.html'
	if request.method == 'GET':
		
		return render(request, template)

	if request.method=='POST':
		col_names = ['CD_PROC_IMPORTA_HUB','CD_IMPORTACAO_HUB','CD_NIVEL','CD_MEDICAO','CD_MEDICAO_PLANTIO','CD_MEDICAO_PARCELA','ID_REGIAO','ID_PROJETO','CD_TALHAO','NRO_PARCELA','NUM_FILA','NUM_ARVORE','NUM_FUSTE','TIP_ARV','CAP','HT']
		#Obtem os ids que ja estão no banco de dados
		ids_db = list(np.unique(Id_hub.objects.values_list('CD_PROC_IMPORTA_HUB', flat=True)))
		ids_db = [int(elem) for elem in ids_db]
		

	
		#Salva o csv do formulário na variável csv_file
		csv_files = request.FILES.getlist('files')

		#FALTA FAZER CHECAGEM SE TODOS SÃO CSV
		#obtem os ids que o usuário subiu com base no nome dos csvs
		ids_list = []
		for i in csv_files:
			ids_list.append(int(re.findall(r'\d+',str(i))[0]))
		
		ids_new=[]
		for i in ids_list:
			if i not in ids_db:
				ids_new.append(i)
		#Lê os csvs e compila somente os que forem ids novos
		c=0
		data_set_df = pd.DataFrame(columns=col_names)
		for csv in csv_files:
			if re.findall(r'\d+',str(csv))[0] in str(ids_new):
				data_set=csv.read().decode("latin1")
				io_string = io.StringIO(data_set)
				data = pd.read_csv(io_string, delimiter=';', quotechar='|')
				data.columns=col_names
				if c==0:
					data_set_df = data
					c=c+1
				else:
					data_set_df = pd.concat([data_set_df,data],ignore_index=True)
					c=c+1
		#cria a tabela resumo
		#transforma o compilado em json para exibir no html
		df_count = data_set_df.groupby('CD_PROC_IMPORTA_HUB').agg({'CD_MEDICAO': 'nunique', 'CD_MEDICAO_PARCELA': 'nunique', 'ID_PROJETO': 'nunique', 'CD_TALHAO': 'nunique'})
		df_count.loc['TOTAL'] = df_count.sum()
		json_records = df_count.reset_index().to_json(orient ='records')
		data_count = json.loads(json_records)

		data_set_df['PROJETO_TALHAO'] =data_set_df['ID_PROJETO'].apply(lambda x: str(x).zfill(3)) + '-' + data_set_df['CD_TALHAO']
		projetos = np.unique(data_set_df['PROJETO_TALHAO'])
		plots=[]	
		for i in np.unique(ids_new):
			plots.append(generate_scatter_plot(i,data_set_df))
		context = {'data_count':data_count,'projeto_talhao':projetos,'plots':plots}
		return render(request,template,context)
			
def show_plots(request):
	return render('base/show_plots.html')




# plots = []
		# for id in ids_new:
		#     plots.append(generate_scatter_plot(id,data_set_df))



# def upload_csv(request):
# 	template = 'base/aplicar_rna.html'
# 	prompt = {
# 		'order':'mensagem do prompt order'
# 	}

# 	if request.method == 'GET':
# 		return render(request,template,prompt)
	
# 	#Salva o csv do formulário na variável csv_file
# 	csv_file = request.FILES.get('files')

# 	#Checar se é um csv
# 	if not csv_file.name.endswith('.csv'):
# 		messages.error(request,"O arquivo que esta tentando subir não é um csv")
# 		return render(request,template,prompt)

# 	#Lê o csv e salva em data_set
# 	data_set = csv_file.read().decode("UTF-8")
# 	io_string = io.StringIO(data_set)
# 	next(io_string)

# 	for column in csv.reader(io_string,delimiter=';',quotechar="|"):
# 		_, created = Contact.objects.update_or_create(
# 			first_name = column[0],
# 			last_name = column[1],
# 			email = column[2],
# 			ip_address = column[3],
# 			message = column[4]
# 		)
# 	#Transformar em data_frame
# 	data_set_df = pd.read_csv(io.StringIO(data_set), delimiter=';', quotechar='|')
# 	#Renomear colunas
# 	colnames = ['first_name','last_name','email','ip_address','message']
# 	data_set_df.columns = colnames

# 	json_records = data_set_df.reset_index().to_json(orient ='records')
# 	data = []
# 	data = json.loads(json_records)
# 	context = {'data_set': data}

# 	return render(request,template,context)


