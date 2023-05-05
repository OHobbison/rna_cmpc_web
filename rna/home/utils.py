import matplotlib.pyplot as plt 
from io import BytesIO
import base64


def get_graph():
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	buffer.seek=0
	plt.close()
	image_png = buffer.getvalue()
	graph=base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffer.close()
	return graph

def generate_scatter_plot(id,data_set_df):
	plt.switch_backend('AGG')
	plt.figure(figsize=(10,5))
	data = data_set_df[data_set_df['CD_PROC_IMPORTA_HUB']==id]
	x = data['CAP']/10/3.1415
	y = data['HT']/10
	plt.scatter(x, y)
	plt.xlabel('DAP (cm)')
	plt.ylabel('HT (m)')
	plt.title('Id hub: {}'.format(id))
	plt.grid(linestyle = '--', linewidth = 0.5)
	plt.xticks(rotation=45)
	plt.xlim(left=0)   # set the minimum limit for x-axis to 0
	plt.ylim(bottom=0) # set the minimum limit for y-axis to 0
	plt.tight_layout()
	graph=get_graph()
	return graph
	