CREATE TABLE Questions (Type INTEGER, QuestionID INTEGER, Sentence TEXT, Token TEXT) WITH (OIDS=TRUE);
CREATE TABLE Actions_back (Action_no INTEGER, ActionName TEXT, ActType TEXT, Generates TEXT, Complexity TEXT, Recipe TEXT, Context_No INTEGER) WITH (OIDS=TRUE);
CREATE TABLE Contexts (ContextId INTEGER, Name TEXT, Host TEXT, AppServer TEXT, ServiceName TEXT, Configuration TEXT) WITH (OIDS=TRUE);
CREATE TABLE reference_layer_view (RefID INTEGER, RefType TEXT, LayerId INTEGER, Filter TEXT, SearchField TEXT, Description TEXT, LayerName TEXT, LayerType TEXT, Category TEXT, Symbology TEXT, IDField TEXT, LabelField TEXT, Workspace TEXT, Context-No INTEGER) WITH (OIDS=TRUE);
CREATE TABLE LayerAttributes (LayerID INTEGER, SelectedAttributes TEXT) WITH (OIDS=TRUE);
CREATE TABLE Connection (Name TEXT, IP TEXT) WITH (OIDS=TRUE);
CREATE TABLE LayerInfo (LayerID INTEGER, LayerName TEXT, LayerType TEXT, Category TEXT, Symbology TEXT, IDField TEXT, LabelField TEXT, Workspace TEXT, Context-No INTEGER) WITH (OIDS=TRUE);
CREATE TABLE DisplayGroups (Context INTEGER, Layer INTEGER, Display TEXT) WITH (OIDS=TRUE);
CREATE TABLE Actions (Action_no INTEGER, ActionName TEXT, ActType TEXT, Generates TEXT, Complexity TEXT, Recipe TEXT, Context_No INTEGER) WITH (OIDS=TRUE);
CREATE TABLE Phrases_back (PID INTEGER, Phrase TEXT, Type TEXT, ActionName TEXT, Alias TEXT, RefID TEXT, ContextId INTEGER) WITH (OIDS=TRUE);
CREATE TABLE referenceInfo (RefID INTEGER, RefType TEXT, LayerId INTEGER, Filter TEXT, SearchField TEXT, SearchPhrase TEXT, ScaleFactor INTEGER) WITH (OIDS=TRUE);
CREATE TABLE Phrases (PID INTEGER, Phrase TEXT, Type TEXT, ActionName TEXT, Alias TEXT, RefID TEXT, ContextId INTEGER) WITH (OIDS=TRUE);
CREATE TABLE Symbology (ParameterName TEXT, ParameterValue TEXT, FillColor TEXT, FillStyle TEXT, FillInterval TEXT, BoundaryStyle TEXT) WITH (OIDS=TRUE);
