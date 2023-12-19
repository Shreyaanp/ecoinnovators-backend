import dash
import os
from scrapeData import *

from dash import dcc, html, callback
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

base_dir = "Scraped/"

app = dash.Dash("Scraper CRON")
app.title = "Scraper 2.1"
app.layout = html.Div([
	html.Div([
		html.Button(
			"Add Resource",
			id = "add-link",
			n_clicks = 0
		),
		html.Button(
			"Remove Last Resource",
			id = "rem-link",
			n_clicks = 0
		),

		html.Button(
			"Download Resources",
			id = "dl-link",
			n_clicks = 0
		),

		html.Div([], id = "resources")
	], id = "resource-container"),

	html.Div([
		html.Button(
			"Delete Selected",
			id = "file-delete",
			n_clicks = 0
		),
		html.Div(id = "file-list")
	]),
	html.P(id = "dummy-output"),
	html.P(id = "dummy-output-2"),
	dcc.Store(
		id = "link-url-count",
		storage_type = "local",
		data = 0
	),
	dcc.Interval(
		id = "interval-component",
		interval = 2000,
		n_intervals = 0
	)
])

# Function to dynamically add and remove text boxes
@app.callback([
	Output("resources", "children"),
	Output("link-url-count", "data")
], [
	Input("add-link", "n_clicks"),
	Input("rem-link", "n_clicks"),	
],
	State("resources", "children")
)
def update_resource_link(add_click, rem_click, curr_links):
	changes = dash.callback_context.triggered_id
	if changes == None:
		return curr_links, [len(curr_links)]
	if "add-link" in changes:
		field = dcc.Input(
			id = f"link-url-{len(curr_links)}",
			type = "text",
			placeholder = "/resource/?"
		)

		curr_links.append(field)
	elif "rem-link" in changes:
		curr_links = curr_links[:-1]

	return curr_links, [len(curr_links)]

@app.callback(
	Output("dummy-output", "children"),
	Input("dl-link", "n_clicks"),
	State("resources", "children"),
)
def download_resources(dl_btn, links):
	urls = [l['props']['value'] for l in links if l['props']['id'].startswith('link-url-')]
	for url in urls:
		print(url)
		dataset_url = url_root + url
		download_file(dataset_url, local_folder_path)
	return [""]


def get_file_list():
	return [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]

@app.callback(
	Output("file-list", "children"),
	Input("interval-component", "n_intervals")
)
def update_file_list(n_intervals):
	files = get_file_list()

	if not files:
		return []

	children = [
		html.Div([
			dcc.Checklist(
				id = {
					"type": "file-select",
					"index": i
				}, options = [{
					"label": "",
					"value": file
				}]
			),
			html.P(file)
		]) for i, file in enumerate(files)
	]

	return children

@app.callback(
	Output("dummy-output-2", "children"),
	Input("file-delete", "n_clicks"),
	[State({'type': 'file-select', 'index': ALL}, 'value')]
)
def delete_selected_file(n_clicks, files):
	if n_clicks > 0 and files:
		to_delete = [f[0] for f in files if f]
		for f in to_delete:
			print(os.remove(base_dir + f))
	else:
		raise PreventUpdate
	return [""]

if __name__ == "__main__":
	app.run_server(debug = True)