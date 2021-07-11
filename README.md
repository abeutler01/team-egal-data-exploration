# team-egal-data-exploration

Dieses Projekt dient der Entwicklung eines Smalltalk-Chatbots, welcher dazu in der Lage sein soll, auf Input in Form von Texteingaben algorhitmusgesteuert passende Antworten in Form von Text als Output zurückzugeben. 



-Ordnerstruktur 

Das Repository ist wie folgt aufgebaut:

- Im Ordner Archive befinden sich die Jupyter Notebooks, welche zum lernen des Cluster- und Klassifikator-Modells genutzt wurden.
- Im Ornder DataExports befindnen sich die aus dem Clusterings entstandenen annotierten Datensätze. 
- Im Ordner Experimental befinden sich Jupyter-Notebooks, in denen verschiedene Cluster- und Klassifikations-Methoden ausprobiert wurden. 
- Der Ordner Chatot_Complete.zip enthält die Chatbot_app als Python-File, sowie die nötigen Datensätze bestehend aus den Clustern und den vorgefertigten Antworten.



-Hinweise zur Ausführung des Codes 

Die ausführbare Python-Datei mit der Bezeichnung „Chatbot_app.py“ findet sich im GitHub Repository im Ordner „Chatbot_Complete“. 
Diesen Ordner als ganzen downloaden und lokal speichern. Darauf die Python-Datei mit der IDE ihres Vertrauens öffnen und darauf achten, dass sich im selben Ordner wie die Python-Datei auch die CSV-Dateien „Answers.csv“ und „cluster_model.csv“ befinden. 
Für die Ausführung des Codes sind die Python Libraries pandas, gensim, spaCy und das Framework Scikit erforderlich, falls nicht schon geschehen, diese downloaden. 
Dann den Code ausführen, wenn die oben genannten Schritte durchgeführt wurden, sollte die Kommandozeile folgenden Text zurückggeben: " Hello, this is SmallTalkBot, I am booting up, please be patient.". Dann müssen Sie sich noch einen Moment gedulden, bis alles geladen wurde. Danach steht der Chatbot zu Ihrer Verfügung! 
