BEGIN TRANSACTION;

INSERT INTO Questions VALUES(2,1,'I have the following data for . Which would you like to see?','6,Phrase,7,RefIDs');
INSERT INTO Actions_back VALUES(10,'ShowMap','Action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Show_a_new_map" Type="Complex" Generates="">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter="extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="layers" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
  <PARA name="Extent" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature"/>
        <THEMETYPE type="envelop, shape, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Refresh_Map" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(11,'IdentifyLayerFromSpeech','ID_PARA','Layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="4" context="1" Name="IdentifyLayerFromSpeech" Type="Complex" Generates="layer">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<PARAMETER>
    <PARA name="layers" multiple="yes" required="yes">
       <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
       </DESCRIPTION>
       <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
    </PARA>
</PARAMETER>
    <SUBACTIONS order="true">
             <SUBACT act="SearchLayerFromSpeech" Type="Basic"/>
             <SUBACT act="ClarifyLayer" Type="Basic"/>
             <SUBACT act="SetLayerParameter" Type="Basic"/>
    </SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(12,'IdentifyFeatureFromSpeech','ID_PARA',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(13,'IdentifyShapeFromGesture','ID_PARA',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(14,'AskParameter','ASK',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(15,'ClarifyFromChoice','Clarify',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(16,'RefreshMap','ACTION',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(17,'SearchLayerFromSpeech','ACTION',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(18,'ClarifyLayer','Clarify',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(20,'IdentifyLayerGroupClarify','ID_PARA',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="4" context="1" Name="IdentifyLayerGroupClarify" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter="layers"/>
</EXTRACT>
<PARAMETER>
    <PARA name="layers" multiple="yes" required="yes">
       <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
       </DESCRIPTION>
       <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
    </PARA>
</PARAMETER>
    <SUBACTIONS order="true">
             <SUBACT act="SearchLayerFromSpeech" Type="Basic"/>
             <SUBACT act="ClarifyLayer" Type="Basic"/>
             <SUBACT act="SetLayerParameter" Type="Basic"/>
    </SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(22,'IdentifyFeatureGroupClarify','ID_PARA',NULL,'Complex',NULL,1);
INSERT INTO Actions_back VALUES(25,'Remove_Map_Elements','action','Layer','Basic',NULL,1);
INSERT INTO Actions_back VALUES(29,'ZoomOut','action','envelop','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="ZoomOut" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter="Extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="Extent" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature"/>
        <THEMETYPE type="envelop, shape, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="ZoomOutMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(19,'IdentifyQuantityFromSpeech','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(27,'ZoomIn','action','envelop','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="ZoomIn" Type="Complex" Generates="extent">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter="Extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="Extent" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature"/>
        <THEMETYPE type="envelop, shape, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="extent" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="ZoomInMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(24,'RemoveMapElements','action','Layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="RemoveMapElements" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="layers" multiple="yes"  required="yes">
      <DESCRIPTION>
            <GEOTYPE type="layer"/>
            <THEMETYPE type="layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
  <PARA name="Extent" multiple="no"  required="no">
      <DESCRIPTION>
         <GEOTYPE type="envelop, shape, polygon, feature, direction"/>
        <THEMETYPE type="envelop, shape, polygon, feature, direction"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="no" changeGestureTo="extent" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Remove_Map_Elements" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(26,'Greeting','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(28,'ZoomInMap','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(31,'Pan','action','envelop','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Pan" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter="extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="Extent" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature, direction"/>
        <THEMETYPE type="envelop, shape, polygon, feature, direction"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="PanMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(32,'PanMap','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(36,'Reset','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(30,'ZoomOutMap','action','envelop','Basic',NULL,1);
INSERT INTO Actions_back VALUES(21,'IdentifyDirectionFromSpeech','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(23,'IdentifyPositionFromGesture','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(33,'IdentifyUnitFromSpeech','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(46,'IdentifyLocationFromHistory','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(50,'SetTimeFrame','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(55,'IdentifyZoneFromSpeech','action','shape','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="IdentifyZoneFromSpeech" Type="Complex" Generates="shape">
<SUBACTIONS order="true" selectOne="true">
      <SUBACT act="EPZZone" Type="Complex"/>
      <SUBACT act="PlumeModel" Type="Complex"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(60,'IdentifyPlumeFromHistory','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(56,'Evacuation','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Evacuation" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="EPZ_Zones,EvacuationZone,ContaminationReadings"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">

  
 <PARA name="EvacuationZone" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape,polygon"/>
        <THEMETYPE type="shape, polygon"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
<PARA name="EPZ_Zones" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="EPZ_Zones"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>
  <PARA name="ContaminationReadings" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="points"/>
        <THEMETYPE type="Readings"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Evacuate" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(57,'Quarantine','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Quarantine" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="Routes"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="Routes" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="Routes"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Evacuate" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(58,'Shelter','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Shelter" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="Routes"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="Routes" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="Routes"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Evacuate" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(34,'Buffer','action','layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Buffer" Type="Complex" Generates="DynamicLayer">
<Parameter Order="false">
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
  <PARA name="layers" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="geometry" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop,shape,polygon,feature"/>
        <THEMETYPE type="geometry"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="distance" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="distance,quantity"/>
        <THEMETYPE type="distance,quantity"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="unit" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="unit"/>
        <THEMETYPE type="unit"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="BufferMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(35,'BufferMap','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(37,'ShowDefaultMap','action','layer','Basic','',1);
INSERT INTO Actions_back VALUES(38,'Confirm','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(39,'Reject','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(40,'UndoPreviousAction','action','layer, extent','Basic',NULL,1);
INSERT INTO Actions_back VALUES(41,'RadioactiveParticulateRelease','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="RadioActive_Particulate_Release" Type="Complex">

<EXTRACT>
<TYPE Name="layer" Parameter="location, EPZ_Zones, PlumeModel"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>

<Parameter Order="false">

  <PARA name="location" multiple="no" required="yes">
      <DESCRIPTION>
            <GEOTYPE type="feature" />
            <THEMETYPE type="feature" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" 

Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="EPZ_Zones" multiple="yes" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="EPZ_Zones"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>
 <PARA name="PlumeModel" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="PlumeModel"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true" selectOne="true">
      <SUBACT act="Evacuation" Type="Complex"/>
      <SUBACT act="Quarantine" Type="Complex"/>
      <SUBACT act="Shelter" Type="Complex"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(43,'IdentifyLocationByName','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(48,'SetWindCondition','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(49,'DrawWindConditionPolygon','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(52,'GetCurrentWindCondition','action','WindCondition','Basic',NULL,1);
INSERT INTO Actions_back VALUES(53,'GetProjectedWindCondition','action','WindCondition','Basic',NULL,1);
INSERT INTO Actions_back VALUES(60,'SelectLineGesture','action','shape','Basic',NULL,1);
INSERT INTO Actions_back VALUES(65,'IdentifyPopulationInArea','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(61,'GetFieldData','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(65,'SoundSirens','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(63,'IdentifySourceForReadings','action','Location','Basic',NULL,1);
INSERT INTO Actions_back VALUES(64,'SetFieldTeam','action ','FieldTeam','Basic',NULL,1);
INSERT INTO Actions_back VALUES(36,'HighLight','action','layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Highlight" Type="Complex">
<Parameter Order="false">
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
  <PARA name="layers" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="geometry" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="envelop,shape,polygon,feature"/>
        <THEMETYPE type="envelop,shape,polygon,feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="polygon" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="distance" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="quantity"/>
        <THEMETYPE type="quantity"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="unit" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="unit"/>
        <THEMETYPE type="unit"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="HighLightMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(64,'Connect','action','Connection','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Connect" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">

 <PARA name="Destination" multiple="no">
      <DESCRIPTION>
            <GEOTYPE type="FieldTeam" />
            <THEMETYPE type="FieldTeam" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" 

Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="EstablishConnection" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(42,'EvacuationPlan','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Evacuation" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="Routes"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">

 <PARA name="location" multiple="no">
      <DESCRIPTION>
            <GEOTYPE type="feature" />
            <THEMETYPE type="feature" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" 

Ask="yes" RepeatUntilKnown="yes"/>
<DEFAULTSUBPLAN act="IdentifyLocationFromHistory" Type="Basic"/>


  </PARA>

  <PARA name="EPZ_Zones" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="EPZ_Zones"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="Routes" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="Routes"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="Evacuate" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(44,'EPZZone','action','EPZ_Zones','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Buffer" Type="Complex" Generates="DynamicLayer">
<Parameter Order="false">
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
  <PARA name="layers" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="geometry" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop,shape,polygon,feature"/>
        <THEMETYPE type="geometry"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="distance" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="distance,quantity"/>
        <THEMETYPE type="distance,quantity"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

  <PARA name="unit" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="unit"/>
        <THEMETYPE type="unit"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="CreateEPZzone" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(45,'PlumeModel','action','PlumeModel','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="PlumeModel" Type="Complex">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter="extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="location" multiple="no">
      <DESCRIPTION>
            <GEOTYPE type="feature"/>
            <THEMETYPE type="feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="windCondition" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="WindCondition"/>
        <THEMETYPE type="WindCondition"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" Ask="no" RepeatUntilKnown="no"/>
  </PARA>

</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="DrawWindConditionPolygon" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(47,'GetWindCondition','action','shape     ','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="GetWindCondition" Type="Complex">
<Parameter Order="false">

  <PARA name="time" multiple="no">
      <DESCRIPTION>
            <TYPE type="timeFrame"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="SetWindCondition" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(54,'AnswerQuestion','action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="AnswerQuestion" Type="Complex">
<Parameter Order="false">

  <PARA name="QuestionAbout" multiple="no">
      <DESCRIPTION>
            <TYPE type="*"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="GetFuturePlans" Type="Basic"/>
      <SUBACT act="GenerateResponse" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(59,'SpatialQuery','action','Layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Spatial_Query" Type="Complex" Generates="Layer">
<EXTRACT>
<TYPE Name="layers" Parameter="layers"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">

  <PARA name="layers" multiple="yes">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="Geometry" multiple="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, polygon"/>
        <THEMETYPE type="shape, polygon"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="polygon" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="PerformSpatialQuery" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(60,'Readings','action','points','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Readings" Type="Complex" Generates="extent">
<EXTRACT>
<TYPE Name="" Parameter=""/>
<TYPE Name="" Parameter="Extent"/>
</EXTRACT>
<Parameter Order="false">

  <PARA name="Source" multiple="no">
      <DESCRIPTION>
        <GEOTYPE type="point"/>
        <THEMETYPE type="RemoteLocation"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="polygon" Ask="no" RepeatUntilKnown="no"/>
<DEFAULTSUBPLAN act="CheckConnection" Type="Basic"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="GetReadings" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(65,'Select','action','layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Select" Type="Complex" Generates="Layer">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="layers" multiple="yes" required="yes">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
  <PARA name="geometry" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop,shape,polygon,feature"/>
        <THEMETYPE type="envelop,shape,polygon,feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="polygon" Ask="no" RepeatUntilKnown="no" required="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="HighLightMap" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(66,'RetrieveAttributes','action','Information','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Return_Attributes" Type="Complex" Generates="information">
<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="layers" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>
<PARA name="SelectedFeatures" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature"/>
        <THEMETYPE type=" envelop, shape, polygon, feature"/>
      </DESCRIPTION>
        <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="RetrieveAttributeValues" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(67,'PlaceMarker','action','Layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="PlaceMarker" Type="Complex">

<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>

<Parameter Order="false">

  <PARA name="MarkerType" multiple="no" required="no">
      <DESCRIPTION>
            <GEOTYPE type="MarkerType" />
            <THEMETYPE type="MarkerType" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" 

Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="Location" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, point, circle, polygon, feature"/>
        <THEMETYPE type="shape, point , circle, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true" selectOne="true">
      <SUBACT act="CreateMarkerLayer" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(68,'IdentifyMarkerFromSpeech','action','MarkerType','Basic',NULL,1);
INSERT INTO Actions_back VALUES(69,'BroadcastIncident','action','Layer','Basic',NULL,1);
INSERT INTO Actions_back VALUES(70,'AccessMedia','action','Layer','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="AccessMedia" Type="Complex">

<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>

<Parameter Order="false">

  <PARA name="Location" multiple="no" required="no">
      <DESCRIPTION>
            <GEOTYPE type="shape, point, circle, polygon" />
            <THEMETYPE type="shape, point, circle, polygon" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="Media" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="layer"/>
        <THEMETYPE type="layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true" selectOne="true">
      <SUBACT act="AccessMedia" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(71,'Intersect','action','point','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="Intersect" Type="Complex" Generates="">
<EXTRACT>
<TYPE Name="layer" Parameter="layers"/>
<TYPE Name="extent" Parameter="extent"/>
</EXTRACT>
<Parameter Order="false">
  <PARA name="layer" multiple="yes" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer"/>
            <THEMETYPE type="Layer"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

  <PARA name="feature" multiple="no" required="no">
      <DESCRIPTION>
        <GEOTYPE type="envelop, shape, polygon, feature"/>
        <THEMETYPE type="envelop, shape, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" Ask="no" RepeatUntilKnown="no"/>
  </PARA>
</Parameter>
<SUBACTIONS order="true">
      <SUBACT act="FindIntersection" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',1);
INSERT INTO Actions_back VALUES(73,'Disable','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(72,'Contained','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(74,'Contact','action',NULL,'Basic',NULL,1);
INSERT INTO Actions_back VALUES(75,'IdentifyPopulation','action','Information','Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="IdentifyPopulation" Type="Complex">

<EXTRACT>
<TYPE Name="layer" Parameter=""/>
<TYPE Name="extent" Parameter=""/>
</EXTRACT>

<Parameter Order="false">

  <PARA name="Layers" multiple="no" required="no">
      <DESCRIPTION>
            <GEOTYPE type="Layer" />
            <THEMETYPE type="Layer" />
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="no" SpeechInput="Yes" GestureInput="no" changeGestureTo="" Ask="yes" RepeatUntilKnown="yes"/>
  </PARA>

 <PARA name="Location" multiple="no" required="yes">
      <DESCRIPTION>
        <GEOTYPE type="shape, point, circle, polygon, feature"/>
        <THEMETYPE type="shape, point , circle, polygon, feature"/>
      </DESCRIPTION>
      <ID-PARA ActionName="" KeepCurrent="yes" SpeechInput="Yes" GestureInput="yes" changeGestureTo="" 

Ask="no" RepeatUntilKnown="no"/>
  </PARA>

</Parameter>
<SUBACTIONS order="true" selectOne="true">
      <SUBACT act="IdentifyPopulationInArea" Type="Basic"/>
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Contexts VALUES(1,'Florida Hurricane Center','guoray.ist.psu.edu','test5.asp','sdeFloridaJPG','<?xml version="1.0" encoding="UTF-8"?>
<ARCXML version="1.1">
  <CONFIG>
    <ENVIRONMENT>
      <LOCALE country="US" language="en" variant="" />
      <UIFONT color="0,0,0" name="Arial" size="12" style="regular" />
      <SCREEN dpi="96" />
    </ENVIRONMENT>
    <MAP>
      <PROPERTIES>
	<ENVELOPE minx="-85.41614102184502" miny="32.336102412682266" maxx="-83.52436361413271" maxy="33.58670694059946" name="Initial_Extent" />
	<MAPUNITS units="decimal_degrees" />
      </PROPERTIES>
      <WORKSPACES>
	<SHAPEWORKSPACE name="shp_ws-0" directory="C:\ArcIMS\Florida" />
      </WORKSPACES>
      <LAYER type="featureclass" name="County Boundary" visible="true" id="0">
	<DATASET name="SouthCounties" type="polygon" workspace="shp_ws-0" />
	<SIMPLERENDERER>
	  <SIMPLEPOLYGONSYMBOL boundarytransparency="1.0" filltransparency="0.0" boundarycaptype="round" />
	</SIMPLERENDERER>
      </LAYER>
      <LAYER type="featureclass" name="State Boundary" visible="true" id="1">
	<DATASET name="south" type="polygon" workspace="shp_ws-0" />
	<SIMPLERENDERER>
	  <SIMPLEPOLYGONSYMBOL boundarytransparency="1.0" filltransparency="0.0" boundarywidth="3" boundarycaptype="round" boundarycolor="255,200,0" />
	</SIMPLERENDERER>
      </LAYER>
      <LAYER type="featureclass" name="Interstate highways" visible="true" id="2">
	<DATASET name="Interstates" type="line" workspace="shp_ws-0" />
	<SIMPLERENDERER>
	  <SIMPLELINESYMBOL width="2" captype="round" color="102,51,0" />
	</SIMPLERENDERER>
      </LAYER>
      <LAYER type="featureclass" name="Cities" visible="true" id="3">
	<DATASET name="SouthCities" type="point" workspace="shp_ws-0" />
	<SCALEDEPENDENTRENDERER lower="1:1000000" upper="1:10000000">
	  <SIMPLERENDERER>
	    <SIMPLEMARKERSYMBOL color="255,0,255" type="star" width="10" />
	  </SIMPLERENDERER>
	</SCALEDEPENDENTRENDERER>
      </LAYER>
    </MAP>
  </CONFIG>
</ARCXML>');
INSERT INTO reference_layer_view VALUES(1005,'Layer',5,NULL,NULL,'Water bodies in the southern region','South Water','Polygon','hydrology, river',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1002,'Layer',2,NULL,NULL,'County boundaries of four southern states including Georgia, Florida, Alabama, and Southern Caralina','South Counties','Polygon','Administrative boundary, local government',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1001,'Layer',1,NULL,NULL,'State Boundaries','South Sates','Polygon','Administrative boundary',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1004,'Layer',4,NULL,NULL,'Location of cities in four Southern States  (including Georgia, Florida, Alabama, and Southern Caralina)','South cities','Point','Administrative',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3002,'Feature',1,NULL,'STATE_NAME','State names in State Boundary map','South Sates','Polygon','Administrative boundary',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1003,'Layer',3,NULL,NULL,'Interstates highways within four Southern states (including Georgia, Florida, Alabama, and Southern Caralina)','South Interstates','Line','Critical facility, highways',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(2001,'Attribute',2,NULL,'Pop2000','Population by county in year 2000','South Counties','Polygon','Administrative boundary, local government',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(2002,'Attribute',1,NULL,'Pop2000','Population by state in year 2000','South Sates','Polygon','Administrative boundary',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3001,'Feature',2,NULL,'Name','Select counties by Name','South Counties','Polygon','Administrative boundary, local government',NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(2003,'Attribute',0,NULL,'Pop2000','Population by county in year 2000','US States','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1006,'Layer',6,NULL,NULL,'all surge area, including category 1, 2, 3, and tropical storm','All surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1007,'Layer',7,NULL,NULL,'category 1 hurricane surge area in Florida','Category 1 surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1008,'Layer',8,NULL,NULL,'category 2 hurricane surge area in Florida','Category 2 surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1009,'Layer',9,NULL,NULL,' category 3 hurricane surge area in Florida','Category 3 surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1010,'Layer',10,NULL,NULL,'assisted living facilities ','Assisted Living Facilites','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1011,'Layer',11,NULL,NULL,' assisted living facilites in the Category 3 surge area','Assisted Living Facilities in the Flooded Area','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1012,'Layer',12,NULL,NULL,'Population in Florida','Florida Population','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1013,'Layer',13,NULL,NULL,'Block level population in the Florida','Block Level Population in Florida','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1014,'Layer',14,NULL,NULL,'Block level population in the  Category 3 surge area','Block level population in the flooded area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1015,'Layer',15,NULL,NULL,'County level population in the Category 3 surge area','County level population in the flooded area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(2004,'Attribute',13,NULL,'Pop1990','Block level Population by county in year1990','Block Level Population in Florida','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(2005,'Attribute',12,NULL,'Pop100','Population in Florida (Not sure the data)','Florida Population','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3003,'Feature',6,NULL,'Category','Select a feature(s) by Category in all surge area','All surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1016,'Layer',16,NULL,NULL,'Buffer zone of 3 miles to the category 3 surge','Buffer zone of 3 miles to the category 3 surge','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1017,'Layer',17,NULL,NULL,'Category 4 hurricane surge area in Florida','Category 4 hurricane surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1018,'Layer',18,NULL,NULL,'Category 5 hurricane surge area in Florida','Category 5 hurricane surge area','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1019,'Layer',19,NULL,NULL,'Hazardous materials storage facilities in Florida','Hazardous materials storage facilities','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1020,'Layer',20,NULL,NULL,'Hazardous materials storage facilities within Category 4 hurricane surge area in Florida','Hazardous materials storage facilities within category 4 hurricane surge area','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1021,'Layer',21,NULL,NULL,'tropical storm area  in Florida','tropical storms','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1050,'Layer',1,NULL,NULL,'RailRoads of New Jersey','Railroads','Line',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1051,'Layer',2,NULL,NULL,'Roads Of New Jersey','Roads','Line',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3007,'Feature',2,NULL,'HWYNAME','Roads of New Jersey','Roads','Line',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1052,'Layer',0,NULL,NULL,'Image of New Jersey','Image of New Jersey','Polygon',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1053,'Layer',4,NULL,NULL,'Hazmat Facilities of New Jersey','Hazmat Facilities of New Jersey','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(1054,'Layer',6,NULL,NULL,'Cameras','Cameras','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3008,'Feature',7,NULL,'NAME','Exit Numbers','Exit Numbers','Point',NULL,NULL,NULL,NULL,'shp_ws-0',1);
INSERT INTO reference_layer_view VALUES(3009,'Feature',5,NULL,'NAME','Counties','Counties',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO LayerAttributes VALUES(5,'NAME');
INSERT INTO LayerAttributes VALUES(11,'NAME');
INSERT INTO Connection VALUES('Radiation Measurement Team','10.20.30.40');
INSERT INTO LayerInfo VALUES(5,'CITIES','Point',NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO LayerInfo VALUES(1,'STATES','Polygon',NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO LayerInfo VALUES(4,'ROADS','Line',NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO LayerInfo VALUES(3,'RIVERS','Line',NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO LayerInfo VALUES(2,'LAKES','Polygon',NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO DisplayGroups VALUES(1,22,'3,4,6');
INSERT INTO Actions VALUES(10,'PerformEvacuation','Action',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(11,'GuideEvacuation','Action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="11" context="1" Name="GuideEvacuation" Type="Complex">
<SUBACTIONS Order="false">
	      <SUBACT Name="IdentifyDiffLocFromGesture" Type="Basic" Optional="true"/>
      <SUBACT Name="AssignGuideTeam" Type="Basic" Optional="true"/> 
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Actions VALUES(12,'IdentifyDiffLocFromGesture','Action',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(13,'AssignGuideTeam','Action',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(1,'PlanEvacuation','Action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="1" context="1" Name="PlanEvacuation" Type="Complex">
<PARAMETERS Order="false">
 <PARA Name="ImpactedArea" Multiple="false" Type="GeoType" Default="IdentifyImpactedArea">
      <ID_PARA Name="IdentifyImpactedArea" Type="Complex" />
 </PARA>
</PARAMETERS>
<SUBACTIONS Order="true">
      <SUBACT Name="PerformEvacuation" Type="Basic" Optional="true"/>
      <SUBACT Name="GuideEvacuation" Type="Complex" Optional="true"/> 
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Actions VALUES(2,'IdentifyImpactedArea','ID_PARA',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="2" context="1" Name="IdentifyImpactedArea" Type="Complex">
<PARAMETERS Order="false">
 <PARA Name="IncidenceLocation" Multiple="false" Type="GeoType" Default="IdentifyFeatureFromSpeech">
      <ID_PARA Name="IdentifyFeatureFromSpeech" Type="Basic" />
 </PARA>
</PARAMETERS>
<SUBACTIONS Order="false">
      <SUBACT Name="GenerateEPZZone" Type="Complex" Optional="true"/>
      <SUBACT Name="GeneratePlumeModel" Type="Complex" Optional="true"/> 
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Actions VALUES(3,'GenerateEPZZone','Action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="3" context="1" Name="GenerateEPZZone" Type="Complex">
<PARAMETERS Order="false">
 <PARA Name="Distance" Multiple="false" Type="Real" Default="IdentifyQuantityFromSpeech">
      <ID_PARA Name="IdentifyQuantityFromSpeech" Type="Basic" />
 </PARA>
</PARAMETERS>
<SUBACTIONS Order="false">
      <SUBACT Name="CalculateBufferZone" Type="Basic" Optional="false"/> 
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Actions VALUES(4,'GeneratePlumeModel','Action',NULL,'Complex','<?xml version="1.0"?>
<DAVE_GXML version="0.0.1">
<RECIPE id="4" context="1" Name="GeneratePlumeModel" Type="Complex">
<PARAMETERS Order="false">
 <PARA Name="WindCondition" Multiple="false" Type="GeoType" Default="GetCurrentWindCondition">
      <ID_PARA Name="GetCurrentWindCondition" Type="Basic" />
 </PARA>
</PARAMETERS>
<SUBACTIONS Order="false">
      <SUBACT Name="CalculatePlumeModel" Type="Basic" Optional="false"/> 
</SUBACTIONS>
</RECIPE>
</DAVE_GXML>',NULL);
INSERT INTO Actions VALUES(5,'IdentifyFeatureFromSpeech','ID_PARA',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(6,'IdentifyQuantityFromSpeech','ID_PARA',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(7,'CalculateBufferZone','Action',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(8,'CalculatePlumeModel','Action',NULL,'Basic',NULL,NULL);
INSERT INTO Actions VALUES(9,'GetCurrentWindCondition','ID_PARA',NULL,'Basic',NULL,NULL);
INSERT INTO Phrases_back VALUES(344,'place','action','Buffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(345,'incident marker','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(346,'this location','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(347,'mark','action','PlaceMarker',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(348,'this incident','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(349,'fire','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(352,'is this','reference-feature','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(353,'what','action','RetrieveAttributes',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(354,'fire marker','reference-Marker','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(355,'I 78','reference-feature','IdentifyFeatureFromSpeech',NULL,'3007',1);
INSERT INTO Phrases_back VALUES(356,'railroads','reference-layer','IdentifyLayerFromSpeech',NULL,'1050',0);
INSERT INTO Phrases_back VALUES(357,'railroad','reference-layer','IdentifyLayerFromSpeech',NULL,'1050',0);
INSERT INTO Phrases_back VALUES(428,'interstates','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',0);
INSERT INTO Phrases_back VALUES(359,'roads','reference-layer','IdentifyLayerFromSpeech',NULL,'1006',0);
INSERT INTO Phrases_back VALUES(360,'road','reference-layer','IdentifyLayerFromSpeech',NULL,'1006',0);
INSERT INTO Phrases_back VALUES(361,'mccarter highway','reference-feature','IdentifyFeatureFromSpeech',NULL,'3007',4);
INSERT INTO Phrases_back VALUES(362,'ATLANTIC CITY EXWY','reference-feature','IdentifyFeatureFromSpeech',NULL,'3007',4);
INSERT INTO Phrases_back VALUES(363,'New Jersey','reference-layer','IdentifyLayerFromSpeech',NULL,'1052',4);
INSERT INTO Phrases_back VALUES(364,'smoke marker','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(365,'smoke','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(366,'this report','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(367,'hazmat marker','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(368,'hazmat incident','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(369,'the interstates','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',0);
INSERT INTO Phrases_back VALUES(370,'hazmat','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(371,'chemical release','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(372,'potential chemical release','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(501,'block out the map','action','RemoveMapElements',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(416,'this river','reference-feature','IdentifyFeatureFromGesture',NULL,'1004',0);
INSERT INTO Phrases_back VALUES(418,'PEMA','reference-feature','IdentifyFeatureFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(419,'emergency managers','reference-feature','IdentifyFeatureFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(420,'Alert','action','Contact',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(421,'DEP containment team','reference-feature','IdentifyFeatureFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(422,'Dispatch','action','Contact',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(423,'Centre','reference-feature','IdentifyFeatureFromSpeech',NULL,'3009',1);
INSERT INTO Phrases_back VALUES(424,'half','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(425,'state forest','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',1);
INSERT INTO Phrases_back VALUES(426,'state forests','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',1);
INSERT INTO Phrases_back VALUES(427,'urban areas','reference-layer','IdentifyLayerFromSpeech',NULL,'1001',0);
INSERT INTO Phrases_back VALUES(414,'petroleum storage facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1038',1);
INSERT INTO Phrases_back VALUES(429,'waterways','reference-layer','IdentifyLayerFromSpeech',NULL,'1004',0);
INSERT INTO Phrases_back VALUES(430,'these','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(431,'rivers','reference-layer','IdentifyLayerFromSpeech',NULL,'1004',0);
INSERT INTO Phrases_back VALUES(432,'one half','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(433,'Water Treatment Facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1037',0);
INSERT INTO Phrases_back VALUES(434,'buffer around these rivers','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(435,'buffer around these petroleum storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(436,'the selected rivers','reference-feature','IdentifyFeatureFromGesture',NULL,'1030',1);
INSERT INTO Phrases_back VALUES(437,'Hospital','reference-layer','IdentifyLayerFromSpeech',NULL,'1039',1);
INSERT INTO Phrases_back VALUES(438,'in this area','reference-polygon','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(440,'command center marker','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(441,'generic marker','reference-MarkerType','IdentifyMarkerFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(442,'Aerial Images','reference-layer','IdentifyLayerFromSpeech',NULL,'1013,1014,1015,1016,1017,1018',1);
INSERT INTO Phrases_back VALUES(443,'Plume Model','reference-layer','IdentifyLayerFromSpeech',NULL,'1041',1);
INSERT INTO Phrases_back VALUES(25,'remove','action','RemoveMapElements',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(26,'hide','action','HideBuffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(34,'Hello','Action','Greeting',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(17,'Palm Beach','reference-feature','IdentifyFeatureFromSpeech',NULL,'3001',2);
INSERT INTO Phrases_back VALUES(18,'Broward','reference-feature','IdentifyFeatureFromSpeech',NULL,'3001',4);
INSERT INTO Phrases_back VALUES(19,'Dade','reference-feature','IdentifyFeatureFromSpeech',NULL,'3001',0);
INSERT INTO Phrases_back VALUES(13,'waters','reference-layer','IdentifyLayerFromSpeech',NULL,'1005',0);
INSERT INTO Phrases_back VALUES(27,'Display','action','ShowMap',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(47,'Buffer_','action','Buffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(22,'Highways','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',0);
INSERT INTO Phrases_back VALUES(23,'Southern States','reference-feature','IdentifyFeatureGroupClarify','1, 2, 3, 4',NULL,2);
INSERT INTO Phrases_back VALUES(21,'State Boundary','reference-layer','IdentifyLayerFromSpeech',NULL,'1001',2);
INSERT INTO Phrases_back VALUES(1,'Georgia','reference-feature','IdentifyFeatureFromSpeech',NULL,'3002',0);
INSERT INTO Phrases_back VALUES(29,'Good','attitude','Confirm',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(30,'OK','attitude','Confirm',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(6,'counties','reference-layer','IdentifyLayerFromSpeech',NULL,'1002',0);
INSERT INTO Phrases_back VALUES(3,'Florida','reference-feature','IdentifyFeatureFromSpeech',NULL,'3002',2);
INSERT INTO Phrases_back VALUES(7,'cities','reference-layer','IdentifyLayerFromSpeech',NULL,'1010',0);
INSERT INTO Phrases_back VALUES(2,'Alabama','reference-feature','IdentifyFeatureFromSpeech',NULL,'3002',2);
INSERT INTO Phrases_back VALUES(31,'NO','attitude','Reject',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(8,'interstate','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',0);
INSERT INTO Phrases_back VALUES(5,'florida state','reference-feature','IdentifyFeatureFromSpeech','3','3002',2);
INSERT INTO Phrases_back VALUES(11,'states','reference-layer','IdentifyLayerFromSpeech',NULL,'1001',0);
INSERT INTO Phrases_back VALUES(106,'population','reference-attribute','IdentifyAttribute',NULL,'2001',0);
INSERT INTO Phrases_back VALUES(32,'Yes','attitude','Confirm',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(35,'Last','order','SelectOneValue',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(36,'first','order','SelectOneValue',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(33,'OK','attitude','ConfirmValue',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(24,'show','action','ShowMap',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(4,'South Carolina','reference-feature','IdentifyFeatureFromSpeech',NULL,'3002',2);
INSERT INTO Phrases_back VALUES(14,'zoom','action','ZoomIn',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(15,'Closer View','action','ZoomIn',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(107,'population','reference-attribute','IdentifyAttribute',NULL,'2002',0);
INSERT INTO Phrases_back VALUES(16,'Move','action','Pan',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(20,'critical facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1003,1004',0);
INSERT INTO Phrases_back VALUES(108,'population','reference-attribute','IdentifyAttribute',NULL,'2003',0);
INSERT INTO Phrases_back VALUES(37,'zoom out','action','ZoomOutMap',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(38,'Up','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(39,'Down','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(40,'Left','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(41,'Right','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(42,'Here','reference-polygon','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(43,'One','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(44,'Two','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(45,'miles','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(46,'mile','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(25,'show me','action','showMap',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(48,'north','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(49,'south','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(50,'west','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(51,'east','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(52,'northwest','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(53,'northeast','reference-direction','IdentifyDirectionFromSpeech',NULL,'',0);
INSERT INTO Phrases_back VALUES(54,'southwest','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(55,'southeast','reference-direction','IdentifyDirectionFromSpeech',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(56,'reset','action','Reset',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(57,'state boundaries','reference-layer','IdentifyLayerFromSpeech',NULL,'1001',2);
INSERT INTO Phrases_back VALUES(58,'inch','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(59,'inches','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(60,'foot','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(61,'feet','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(62,'Highlight','action','Highlight',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(63,'Three','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(64,'Four','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(65,'Five','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(66,'Six','reference-quantity','IdentifyQuantityFromSpeech',NULL,'',0);
INSERT INTO Phrases_back VALUES(67,'Seven','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(68,'Eight','reference-quantity','IdentifyQuantityFromSpeech',NULL,'',0);
INSERT INTO Phrases_back VALUES(69,'Nine','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(70,'Ten','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(71,'tropical storm','action','ShowDefaultMap',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(72,'areas that will flood','reference-layer','IdentifyLayerFromSpeech',NULL,'1006,1007, 1008, 1009, 1017, 1018,1021',2);
INSERT INTO Phrases_back VALUES(73,'area that will flood','reference-layer','IdentifyLayerFromSpeech',NULL,'1006,1007, 1008, 1009, 1017, 1018,1021',2);
INSERT INTO Phrases_back VALUES(109,'population','reference-attribute','IdentifyAttribute',NULL,'2004',0);
INSERT INTO Phrases_back VALUES(111,'Hillsborough','reference-feature','IdentifyFeatureFromSpeech',NULL,'3001',1);
INSERT INTO Phrases_back VALUES(112,'create','action','Buffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(110,'population','reference-attribute','IdentifyAttribute',NULL,'2005',0);
INSERT INTO Phrases_back VALUES(106,'storm surge flooding zone for a category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(107,'storm surge flooding zone for a category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(108,'hazardous materials storage facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(113,'place buffers','action','Buffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(114,'buffers','action','Buffer',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(115,'population by county','reference-layer','IdentifyLayerFromSpeech',NULL,'1015',0);
INSERT INTO Phrases_back VALUES(116,'inundated assisted living facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',2);
INSERT INTO Phrases_back VALUES(117,'hazmat facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(118,'category three','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(88,'storm surge flood zone for a category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(89,'category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(90,'population within the flooding area','reference-layer','IdentifyLayerFromSpeech','','1014, 1015',0);
INSERT INTO Phrases_back VALUES(91,'population within  flooding area','reference-layer','IdentifyLayerFromSpeech','','1014, 1015',0);
INSERT INTO Phrases_back VALUES(119,'select','action','Select',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(109,'hazardous materials storage facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(121,'inundated the assisted living facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',2);
INSERT INTO Phrases_back VALUES(96,'population by block level','reference-layer','IdentifyLayerFromSpeech','','1014',0);
INSERT INTO Phrases_back VALUES(97,'the population by block level','reference-layer','IdentifyLayerFromSpeech',NULL,'1014',0);
INSERT INTO Phrases_back VALUES(98,'assisted living facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1010',2);
INSERT INTO Phrases_back VALUES(99,'the assisted living facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1010',2);
INSERT INTO Phrases_back VALUES(100,'assisted living facilities within the flooded region','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',2);
INSERT INTO Phrases_back VALUES(101,'the assisted living facilities within the flooded region','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',2);
INSERT INTO Phrases_back VALUES(102,'three mile buffer around the current surge zone','reference-layer','IdentifyLayerFromSpeech',NULL,'1016',0);
INSERT INTO Phrases_back VALUES(122,'assisted living facility','reference-layer','IdentifyLayerFromSpeech',NULL,'1010',2);
INSERT INTO Phrases_back VALUES(123,'a tropical storm','action','ShowDefaultMap',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(105,'this area','reference-polygon','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(124,'population within the flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',0);
INSERT INTO Phrases_back VALUES(125,'population within flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',0);
INSERT INTO Phrases_back VALUES(126,'the population within the flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',2);
INSERT INTO Phrases_back VALUES(127,'the population within flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',2);
INSERT INTO Phrases_back VALUES(128,'the population within flooding area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',2);
INSERT INTO Phrases_back VALUES(129,'the population within the flooding area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',2);
INSERT INTO Phrases_back VALUES(130,'scroll','action','Pan',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(131,'the areas that will flood','reference-layer','IdentifyLayerFromSpeech',NULL,'1006,1007, 1008, 1009, 1017, 1018,1021',2);
INSERT INTO Phrases_back VALUES(132,'the area that will flood','reference-layer','IdentifyLayerFromSpeech',NULL,'1006,1007, 1008, 1009, 1017, 1018,1021',2);
INSERT INTO Phrases_back VALUES(133,'population within the flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',0);
INSERT INTO Phrases_back VALUES(134,'the population within the flooded area','reference-layer','IdentifyLayerFromSpeech',NULL,'1014,1015',2);
INSERT INTO Phrases_back VALUES(135,'the hazardous materials storage facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1019',0);
INSERT INTO Phrases_back VALUES(136,'hazardous materials storage facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(137,'undo','action','UndoPreviousAction',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(138,'tropical storms','reference-layer','IdentifyLayerFromSpeech',NULL,'1021',2);
INSERT INTO Phrases_back VALUES(139,'storm surge flood zone for category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(140,'category four','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(141,'category five','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(143,'storm surge flood zone for category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(142,'storm surge flood zone for a category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(144,'storm surge flooding zone for category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(145,'storm surge flooding zone for a category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(146,'category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(147,'storm surge flood zone for a category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(148,'storm surge flood zone for category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(149,'storm surge flooding zone for a category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(150,'storm surge flooding zone for category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(151,'category five hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1018',2);
INSERT INTO Phrases_back VALUES(152,'storm surge flood zone for a category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(153,'storm surge flooding zone for a category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(154,'storm surge flood zone for category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(155,'storm surge flood zone for a category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(156,'category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(157,'storm surge flood zone for tropical storms','reference-layer','IdentifyLayerFromSpeech',NULL,'1021',2);
INSERT INTO Phrases_back VALUES(158,'storm surge flooding zone for tropical storms','reference-layer','IdentifyLayerFromSpeech',NULL,'1021',2);
INSERT INTO Phrases_back VALUES(159,'those hazmat facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(160,'the storm surge flood zone for a category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(161,'the storm surge flood zone for category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(162,'the storm surge flood zone for the category three hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1009',2);
INSERT INTO Phrases_back VALUES(163,'the hazardous materials storage facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(164,'hazardous materials storage facilities in the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(165,'the hazardous materials storage facilities in the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(166,'hazardous material storage facilities in the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(167,'the hazardous material storage facilities in the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(168,'hazardous material storage facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(169,'the hazardous material storage facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(170,'hazardous materials storage facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(171,'hazardous materials storage facilities in new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(172,'the hazardous materials storage facilities in new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(173,'the hazardous materials storage facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(174,'hazardous material storage facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(175,'hazardous material storage facilities in new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(176,'the hazardous material storage facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(177,'the hazardous material storage facilities in new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(178,'the inundated assisted living facilities','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',0);
INSERT INTO Phrases_back VALUES(179,'that hazardous materials storage facilities in the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(180,'that hazardous materials storage facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(181,'that hazardous materials storage facilities in new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(182,'that hazardous materials storage facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(183,'place_','action','PlaceMarker',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(184,'buffer around these facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(185,'tropical storm','action','ShowDefaultMap',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(186,'buffers around these facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(187,'buffer around each of those hazardous materials storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(188,'buffers around each of those hazardous materials storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(189,'buffer around each of the hazardous materials storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(190,'buffers around each of the hazardous materials storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(191,'buffer around each of those hazardous material storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(192,'buffers around each of those hazardous material storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(193,'buffer around each of the hazardous material storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(194,'buffers around each of the hazardous material storage facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(195,'buffers around each of those facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(196,'buffer around each of those facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(197,'buffers around each of these facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(198,'buffer around each of these facilities','reference-feature','IdenfityShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(199,'the storm surge flood zone for category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(200,'the storm surge flood zone for a category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(201,'storm surge flood zone for the category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(202,'the storm surge flood zone for the category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(203,'the storm surge flooding zone for category four hurricane','reference-layer','IdentifyLayerFromSpeech',NULL,'1017',2);
INSERT INTO Phrases_back VALUES(204,'buffer around these facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(205,'buffers around these facilities','reference-feature','IdentifyShapeFromGesture',NULL,NULL,2);
INSERT INTO Phrases_back VALUES(206,'hazmat facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(207,'the hazmat facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1020',0);
INSERT INTO Phrases_back VALUES(208,'hazmat facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(209,'hazmat facilities within a new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(210,'hazmat facility within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(206,'hazmat facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(300,'radioactive release','action','RadioactiveParticulateRelease',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(303,'the plant','reference-feature','IdentifyLocationFromHistory',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(301,'crystal river nuclear power plant','reference-feature','IdentifyFeatureFromSpeech',NULL,'3004',0);
INSERT INTO Phrases_back VALUES(302,'create EPZ zone','action','EPZZone',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(316,'evacuation plan','action','Evacuation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(305,'over this region','reference-polygon','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(306,'what is','action','AnswerQuestion',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(307,'what are','action','AnswerQuestion',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(311,'projected','reference-timeFrame','SetTimeFrame',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(315,'what are the current wind conditions','action','GetCurrentWindCondition',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(308,'wind condition','action','GetWindCondition',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(309,'wind conditions','action','GetWindCondition',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(310,'current','reference-timeFrame','SetTimeFrame',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(316,'what is the projected wind condition later today','action','GetProjectedWindCondition',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(313,'plume model','reference-shape','PlumeModel',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(316,'twenty','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(317,'thirty','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(318,'fourty','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(314,'Draw','action','IdentifyZoneFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(319,'add','action','PlaceMarker',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(315,'COVE MANOR','reference-feature','IdentifyFeatureFromSpeech',NULL,'3005',0);
INSERT INTO Phrases_back VALUES(321,'within','action','SpatialQuery',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(322,'hazmat facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(323,'hazmat facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(322,'hazmat facilities within new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(323,'hazmat facilities within the new area','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(324,'from here to here','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(320,'projected plume','reference-shape','IdentifyPlumeFromHistory',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(325,'evacuate','action','Evacuation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(326,'EPZ zones','reference-layer','IdentifyLayerFromSpeech',NULL,'2222',0);
INSERT INTO Phrases_back VALUES(327,'get readings','action','Readings',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(328,'connect','action','Connect',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(329,'the region','reference-polygon','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(330,'field checkpoints','reference-feature','IdentifySourceForReadings',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(331,'radiation measurement team','reference-FieldTeam','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(332,'evacuation zone','action','Evacuation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(334,'evacuation routes','reference-layer','IdentifyLayerFromSpeech',NULL,'1024',0);
INSERT INTO Phrases_back VALUES(335,'what is the total population in this area','action','IdentifyPopulationInArea',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(336,'sound the sirens','action','SoundSirens',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(338,'give me','action','RetrieveAttributes',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(339,'these','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(337,'relay the evacuation zones on the EAS radio','action','RelayEvacuationZones',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(340,'this','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(341,'assisted living facility','reference-layer','IdentifyLayerFromSpeech',NULL,'1011',2);
INSERT INTO Phrases_back VALUES(342,'hazmat facility','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',0);
INSERT INTO Phrases_back VALUES(343,'hazardous materials storage facility','reference-layer','IdentifyLayerFromSpeech',NULL,'1053',1);
INSERT INTO Phrases_back VALUES(377,'this marker','reference-shape','IdentifyShapeFromGesture',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(378,'camera','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(502,'miles EPZ','action','EPZzone',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(444,'the selected building','reference-feature','IdentifyFeatureFromGesture',NULL,'1034',1);
INSERT INTO Phrases_back VALUES(445,'Buildings','reference-layer','IdentifyLayerFromSpeech',NULL,'1034',1);
INSERT INTO Phrases_back VALUES(446,'Gas Lines','reference-layer','IdentifyLayerFromSpeech',NULL,'1035,1036',1);
INSERT INTO Phrases_back VALUES(447,'Walkways','reference-layer','IdentifyLayerFromSpeech',NULL,'1033',1);
INSERT INTO Phrases_back VALUES(448,'Streets','reference-layer','IdentifyLayerFromSpeech',NULL,'1031',0);
INSERT INTO Phrases_back VALUES(449,'Parking','reference-layer','IdentifyLayerFromSpeech',NULL,'1032',1);
INSERT INTO Phrases_back VALUES(450,'Send','action','Contact',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(451,'Gas Leak Team','action','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(452,'Radiation Health Team','action','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(453,'Heliport','reference-layer','IdentifyLayerFromSpeech',NULL,'1040',1);
INSERT INTO Phrases_back VALUES(454,'Fire and Police','action','SetFieldTeam',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(455,'kilometer','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(456,'kilometers','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(457,'meter','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(458,'meters','reference-unit','IdentifyUnitFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(459,'Police','action','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(460,'Fly in','action','Contact',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(461,'Disaster Medical Assistants','action','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(462,'Places','reference-layer','IdentifyLayerFromSpeech',NULL,'1023',0);
INSERT INTO Phrases_back VALUES(463,'fifteen','reference-quantity','IdentifyQuantityFromSpeech',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(465,'OPP','action','SetFieldTeam',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(466,'Gas Valves','reference-layer','IdentifyLayerFromSpeech',NULL,'1036',1);
INSERT INTO Phrases_back VALUES(467,'disabled','action','Disable',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(468,'contained','action','Contained',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(469,'Safe Buildings','reference-layer','IdentifyLayerFromSpeech',NULL,'1042',1);
INSERT INTO Phrases_back VALUES(336,'what is the population','action','IdentifyPopulation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(337,'what will the population be','action','IdentifyPopulation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(503,'evacuate people to','action','PlaceMarker',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(504,'we need to','action','ShowMap',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(506,'evacuate this area','reference-layer','IdentifyLayerFromSpeech',NULL,'1042',1);
INSERT INTO Phrases_back VALUES(505,'have been disabled','action','Highlight',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(507,'evacuation','action','Evacuation',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(379,'cameras','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(380,'the camera','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(381,'the cameras','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(382,'a camera','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(383,'a cameras','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(384,'all known live video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(385,'video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(386,'all video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(387,'all known video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(388,'broadcast','action','BroadcastIncident',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(389,'access','action','AccessMedia',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(390,'exit fifty seven','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(391,'exit fifty eight a','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(392,'exit fifty eight b','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(393,'exit fifty nine a','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(394,'exit fifty nine b','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(395,'exit sixty','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(396,'exit fifty six','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(397,'intersection','action','Intersect',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(398,'image of new jersey','reference-layer','IdentifyLayerFromSpeech',NULL,'1052',4);
INSERT INTO Phrases_back VALUES(399,'I seventy eight','reference-feature','IdentifyFeatureFromSpeech',NULL,'3007',1);
INSERT INTO Phrases_back VALUES(400,'interstate seventy eight','reference-feature','IdentifyFeatureFromSpeech',NULL,'3007',4);
INSERT INTO Phrases_back VALUES(401,'give','action','RetrieveAttributes',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(402,'live video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',0);
INSERT INTO Phrases_back VALUES(403,'all live video sources','reference-layer','IdentifyLayerFromSpeech',NULL,'1054',1);
INSERT INTO Phrases_back VALUES(404,'exit fifty six a','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(405,'exit fifty six b','reference-feature','IdentifyFeatureFromSpeech',NULL,'3008',0);
INSERT INTO Phrases_back VALUES(410,'Pan','action','Pan',NULL,NULL,0);
INSERT INTO Phrases_back VALUES(411,'Pennsylvania','reference-feature','IdentifyFeatureFromSpeech',NULL,'3010',1);
INSERT INTO Phrases_back VALUES(412,'Super Highway','reference-layer','IdentifyLayerFromSpeech',NULL,'1003',0);
INSERT INTO Phrases_back VALUES(413,'Petroleum tank leak','reference-layer','IdentifyLayerFromSpeech',NULL,NULL,1);
INSERT INTO Phrases_back VALUES(415,'township','reference-layer','IdentifyFeatureFromGesture',NULL,NULL,0);
INSERT INTO referenceInfo VALUES(1001,'Feature',5,NULL,'CITY_NAME','Salt Lake City',8);
INSERT INTO Phrases VALUES(11,'zoom out','map-action','ZoomOutMap',NULL,NULL,NULL);
INSERT INTO Phrases VALUES(12,'zoom in','map-action','ZoomInMap',NULL,NULL,NULL);
INSERT INTO Phrases VALUES(13,'order evacuation','action','PerformEvacuation',NULL,'0',1);
INSERT INTO Phrases VALUES(14,'evacuation difficulty','action','IdentifyDiffLocFromGesture',NULL,'0',1);
INSERT INTO Phrases VALUES(15,'go to site','action','AssignGuideTeam',NULL,'0',1);
INSERT INTO Phrases VALUES(10,'fifty','reference-quantity','IdentifyQuantityFromSpeech',NULL,'0',1);
INSERT INTO Phrases VALUES(2,'crystal river nuclear power plant','reference-feature','IdentifyFeatureFromSpeech',NULL,'1001',1);
INSERT INTO Phrases VALUES(1,'evacuation','action','PlanEvacuation',NULL,NULL,1);
INSERT INTO Phrases VALUES(3,'ten','reference-quantity','IdentifyQuantityFromSpeech',NULL,'0',1);
INSERT INTO Phrases VALUES(4,'twenty','reference-quantity','IdentifyQuantityFromSpeech',NULL,'0',1);
INSERT INTO Phrases VALUES(5,'thirty','reference-quantity','IdentifyQuantityFromSpeech',NULL,'0',1);
INSERT INTO Phrases VALUES(6,'forty','reference-quantity','IdentifyQuantityFromSpeech',NULL,'0',1);
INSERT INTO Phrases VALUES(7,'epz','action','GenerateEPZZone',NULL,NULL,1);
INSERT INTO Phrases VALUES(8,'current wind condition','reference-attribute','GetCurrentWindCondition',NULL,'0',1);
INSERT INTO Phrases VALUES(9,'plume model','action','GeneratePlumeModel',NULL,NULL,1);
INSERT INTO Symbology VALUES('EPZ_Zone            ','10                  ','255       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','20                  ','245       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','30                  ','235       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','40                  ','225       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','50                  ','215       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','60                  ','205       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','70                  ','195       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','80                  ','185       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','90                  ','175       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('EPZ_Zone            ','100                 ','165       ','7         ',NULL,NULL);
INSERT INTO Symbology VALUES('PlumeModel          ',NULL,NULL,'6         ','3         ',NULL);
COMMIT;
