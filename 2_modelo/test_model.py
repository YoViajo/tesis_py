## Ref: https://www.kdnuggets.com/2021/06/create-deploy-sentiment-analysis-app-api.html
## Modelo de análisis de sentimiento


from transformers import pipeline

#text = 'i love this movie!!! :)'
#text = 'Ideal para ir a pasar el dia con familias o con amigos. Excelentes opciones de pisicnas y areas al aire libre para disfrutar de un dia al sol.'
#text = 'La entrada es carísima para la economía boliviana . No orquídeas en el orquideareo . El aviario son un par de tucanes y loros . Solo había una piscina funcionando y llena de pelos y sucia . Los baños no están limpios. De verdad para los casi 20 usd de la entrada no merece la pena . Detestable'
#text = 'Hemos venido al parque a la 1:15 p.m. una señorita salió y dijo que estaban llenos y que retornáramos a las 3:00 p.m. de la tarde, que a esa hora la entrada estaría reducida a 50 bolivianos y que podríamos diafrutar de las instalaciones gratamente y brindarían un buen servicio. Hemos regresado a esa hora y ahora no quieren dejarnos entrar a pesar que durante este tiempo he visto salir varios autos con personas. Hasta el momento solo sale un guardia y nos dice que la señorita se equivocó y que recién a las 4:00 p.m. nos dejarán entrar. Muy mal que nos engañen así y no haya respeto y coherencia de parte de la empresa que maneja el parque. Me hacen gastar dos servicios de movilidad y espera, perder el tiempo y pasar momentos desagradables. Mejor es decir la verdad, que no se podrá entrar y evitar todo este disgusto.'
#text = 'Mucha espectativa, sin embargo desde en inicio el trato fue insuficiente. Mala atención, infraestructura no funcional me agrado el aviario, orquidiario pero por el resto deja mucho que desear. Ni quejandose a los mismos funcionarios se logra atender las demandas. No lo recomendo a nadie que se dediquen a investigar y preservar y cuando piensen en dar un servicio recuerden que deben cumplir con las espectativas de los clientes.'
text = 'Teniamos muchas expectativas sobre este hotel y resulto ser espantoso:Piscinas sucias y heladas,personal sin actitud a atender al turista como corresponde y las habitaciones sucias de telas de arañas y llenas de hojas porque no barren la entrada..esta super mal ubicado lejos de todo con poca iluminacion,el baño esta construido en piedra que al ser tan chiquito te raspas toso mientras te bañas. Esta lleno de gatos que te molestan todo el tiempo y ademas el desayuno es escacisimo...tenes que gastar mucho dinero en taxi porque queda lejos de todo y en una zona muy fea.El guia que te da la vista es un chiste ..en 5 minutos y apurad te muestra todo .NO VOLVERIA muy caro para lo que ofrece y que pongan personal para que limien las piscinas'

# Instantiate a pipeline object with our task and model passed as parameters
nlp = pipeline(task='sentiment-analysis', 
               model='nlptown/bert-base-multilingual-uncased-sentiment')

# Pass the text to our pipeline and print the results
print(f'{nlp(text)}')
