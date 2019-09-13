import csv

list= []

with open('image.csv', newline="") as f:
    manifest = csv.reader(f, delimiter=",")
    for cotes in manifest:
        list.append(cotes)

for row in list:
    file_name = row[8]+".json"
    nouveau_fichier = open(file_name, 'w+')  # open file in write mode
    nouveau_fichier.write("""{
  "@context": "http://iiif.io/api/presentation/2/context.json",
  "@type": "sc:Manifest",
  "@id": "http://localhost:8000/manifest/"""+row[8]+""".json",
  "label": "archive",
  "description": "Documents d'archives relatifs à la débâcle du Giétroz en 1818",
  "metadata": [
    {
      "label": "cote",
      "value": \""""+row[1]+"""\"
    },
    {
      "label": "type",
      "value": \""""+row[2]+"""\"
    },
    {
      "label": "émetteur",
      "value": \""""+row[3]+"""\"
    },
    {
      "label": "destinataire",
      "value": \""""+row[4]+"""\"
    },
    {
      "label": "date",
      "value": \""""+row[5]+"""\"
    },
    {
      "label": "lieu",
      "value": \""""+row[6]+"""\"
    },
    {
      "label": "sujet",
      "value": \""""+row[7]+"""\"
    }
  ],
  "attribution": "Archives de l'Etat du Valais",
  "sequences": [
    {
      "@type": "sc:Sequence",
      "viewingHint": "individuals/paged",
      "viewingDirection": "left-to-right",
      "canvases": [
                {"@type": "sc:Canvas",
                "@id": "http://localhost:8182/iiif/2/CH-""" + row[9] + """/canvas/1",
                "label": "cover",
                "width": 6099,
                "height": 8599,
                "images":[{
                        "@type": "oa:Annotation",
                        "motivavtion": "sc:painting",
                        "on": "http://localhost:8182/iiif/2/CH-""" + row[9] + """/canvas/1",
                        "resource": {
                                    "@type": "dctypes:Image",
                                    "@id": "http://localhost:8182/iiif/2/CH-""" + row[9] + """/full/full/0/default.jpg",
                                    "service": {
                                                "@context": "http://iiif.io/api/image/2/context.json",
                                                "@id": "http://localhost:8182/iiif/2/CH-""" + row[9] + """\",
                                                "profile": "http://iiif.io/api/image/2/level2.json"
                                                }
                                    }
                        }]
                },
                {"@type": "sc:Canvas",
                "@id": "http://localhost:8182/iiif/2/CH-""" + row[10] + """/canvas/1",
                "label": "cover",
                "width": 6099,
                "height": 8599,
                "images":[{
                        "@type": "oa:Annotation",
                        "motivavtion": "sc:painting",
                        "on": "http://localhost:8182/iiif/2/CH-""" + row[10] + """/canvas/1",
                        "resource": {
                                    "@type": "dctypes:Image",
                                    "@id": "http://localhost:8182/iiif/2/CH-""" + row[10] + """/full/full/0/default.jpg",
                                    "service": {
                                                "@context": "http://iiif.io/api/image/2/context.json",
                                                "@id": "http://localhost:8182/iiif/2/CH-""" + row[10] + """\",
                                                "profile": "http://iiif.io/api/image/2/level2.json"
                                                }
                                    }
                        }]
                },
                  {"@type": "sc:Canvas",
                "@id": "http://localhost:8182/iiif/2/CH-""" + row[11] + """/canvas/1",
                "label": "cover",
                "width": 6099,
                "height": 8599,
                "images":[{
                        "@type": "oa:Annotation",
                        "motivavtion": "sc:painting",
                        "on": "http://localhost:8182/iiif/2/CH-""" + row[11] + """/canvas/1",
                        "resource": {
                                    "@type": "dctypes:Image",
                                    "@id": "http://localhost:8182/iiif/2/CH-""" + row[11] + """/full/full/0/default.jpg",
                                    "service": {
                                                "@context": "http://iiif.io/api/image/2/context.json",
                                                "@id": "http://localhost:8182/iiif/2/CH-""" + row[11] + """\",
                                                "profile": "http://iiif.io/api/image/2/level2.json"
                                                }
                                    }
                        }]
                },
                  {"@type": "sc:Canvas",
                "@id": "http://localhost:8182/iiif/2/CH-""" + row[12] + """/canvas/1",
                "label": "cover",
                "width": 6099,
                "height": 8599,
                "images":[{
                        "@type": "oa:Annotation",
                        "motivavtion": "sc:painting",
                        "on": "http://localhost:8182/iiif/2/CH-""" + row[12] + """/canvas/1",
                        "resource": {
                                    "@type": "dctypes:Image",
                                    "@id": "http://localhost:8182/iiif/2/CH-""" + row[12] + """/full/full/0/default.jpg",
                                    "service": {
                                                "@context": "http://iiif.io/api/image/2/context.json",
                                                "@id": "http://localhost:8182/iiif/2/CH-""" + row[12] + """\",
                                                "profile": "http://iiif.io/api/image/2/level2.json"
                                                }
                                    }
                        }]
                }
                ]
    
    }]
    }""")
    nouveau_fichier.close()

