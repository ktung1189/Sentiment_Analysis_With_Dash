stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
              'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
              'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
              'itself', 'they', 'them', 'their', 'theirs', 'themselves',
              'what', 'which', 'who', 'whom', 'this', 'that', 'these',
              'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
              'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
              'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
              'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
              'against', 'between', 'into', 'through', 'during', 'before', 'after',
              'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
              'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here',
              'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
              'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
              'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
              'will', 'just', 'don','should', 'now','https',"'s",'...', "whats'",
              "rt","whats","n't","de","'m","un","en","``","dedic","twittermoments",
              "amp","e","y","o","ce","retweet","sur","na","el","1","2","3","4",
              "5","6","7","8","9","0","ca","nao","se","com","los","u","des","-",
              "--","'","''","la","como","con","segundo",'de', 'la', 'que', 'el',
              'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para',
              'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus',
              'le', 'ya', 'o', 'este', 'sí', 'porque', 'esta', 'entre', 'cuando',
              'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde',
              'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les',
              'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto',
              'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras',
              'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada',
              'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo',
              'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas',
              'nosotras', 'vosostros', 'vosostras', 'os', 'mío', 'mía', 'míos',
              'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos',
              'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro',
              'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás',
              'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos',
              'estéis', 'estén', 'estaré', 'estarás', 'estará', 'estaremos',
              'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos',
              'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos',
              'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos',
              'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos',
              'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviésemos',
              'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados',
              'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'haya',
              'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá', 'habremos',
              'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían',
              'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo',
              'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos',
              'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis',
              'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy',
              'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis',
              'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería',
              'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais',
              'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera',
              'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos',
              'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos',
              'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos',
              'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan',
              'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán',
              'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía',
              'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo',
              'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos',
              'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis',
              'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened',
              "ve","dia","algun","ningun","pregunta","segunda","bugun","mas","da",
              "alguna","si","bur","bu","icin","bir","um","know","mais","pra","time","q","em",
              "re","11","isnt","wan","ver","like","'re","m","'ve","bec","n","twt","kca","c","a",
              "b","d","e","f","g","h","i","j","k","l","m","n","o",
              "p","q","r","s","t","u","v","w","x","y","z"]
