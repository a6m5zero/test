<!DOCTYPE html>
<html>
<head>
 	<meta charset="utf-8"> 
	<title>Гороскоп</title>
	<link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
	<script src="/static/jquery-3.5.1.min.js"></script>
</head>
<body>
	<div class="container">
	<h1>Что день {{ date }} готовит</h1>
		% if special_date:
			<h2>Сегодня супер особенный день!</h2>
		% end
		% for pred in predictions:
			<p>{{ pred }}</p>
		% end
	</div>
</body>
<script language="javascript">
	console.log( {{ x }} );
</script>
</html>