# team-egal-data-exploration

Dieses Projekt dient der Entwicklung eines Smalltalk-Chatbots, welcher dazu in der Lage sein soll, auf Input in Form von Texteingaben algorhitmusgesteuert passende Antworten in Form von Text als Output zurückzugeben. 



Ordnerstruktur 

Das Repository ist wie folgt aufgebaut:

- Im Ordner Archive befinden sich die Jupyter Notebooks, welche zum testen des Cluster- und Klassifikator-Methoden genutzt wurden, aber letzlich nicht implementiert wurden.
- Im Ornder DataExports befindnen sich alle aus dem Clusterings entstandenen annotierten Datensätze. 
- Im Ordner Experimental befinden sich Jupyter-Notebooks, in denen verschiedene Cluster- und Klassifikations-Methoden ausprobiert wurden. 
- Die Dokumentation ist als Projektreport.pdf im Hauptordner zu finden

- Der Ordner Chatot_Complete.zip enthält die Chatbot_app als Python-File, sowie die nötigen Datensätze bestehend aus den Clustern und den vorgefertigten Antworten.


Hinweise zur Ausführung des Codes 

- Die ausführbare Python-Datei mit der Bezeichnung „Chatbot_app.py“ findet sich im GitHub Repository im Ordner „Chatbot_Complete“. 
- Diesen Ordner als ganzen downloaden und lokal speichern. 
- Achten sie daruaf, dass sich sich im selben Ordner wie die Python-Datei auch die CSV-Dateien „Answers.csv“ und „cluster_model.csv“ befinden. 
- Nachfolgend kann die Python-Datei via der Kommandozeile oder mit der IDE Ihres Vertrauens öffnen
- Für die Ausführung des Codes sind die Python Libraries pandas, gensim, spaCy und das Framework Scikit erforderlich, falls nicht schon geschehen, diese downloaden. 
- Der Chatbot wurde für Windows ausgelegt, sollte er auf einem MacOS Rechner ausgeführt werden, ersetzen sie die „chatbot_app.py“ durch die „Chatbot_app_macOS.py“ welche im github zu finden ist
- Wenn die oben genannten Schritte durchgeführt wurden, sollte die Kommandozeile folgenden Text zurückggeben: " Hello, this is SmallTalkBot, I am booting up, please be patient.". 
- Dann müssen Sie sich noch einen Moment gedulden, bis alles geladen wurde. Danach steht der Chatbot zu Ihrer Verfügung! 

