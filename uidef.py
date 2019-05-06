uidef="""
<?xml version='1.0' encoding='utf-8'?>
<interface>
  <object class="ttk.Frame" id="base_frame">
    <property name="height">800</property>
    <property name="width">700</property>
    <layout>
      <property name="column">0</property>
      <property name="propagate">True</property>
      <property name="row">1</property>
    </layout>
    <child>
      <object class="ttk.Labelframe" id="label_frame_comm_log">
        <property name="height">200</property>
        <property name="text" translatable="yes">Communication log</property>
        <property name="width">200</property>
        <layout>
          <property name="column">0</property>
          <property name="columnspan">2</property>
          <property name="propagate">True</property>
          <property name="row">2</property>
          <property name="rowspan">2</property>
        </layout>
        <child>
          <object class="tk.Text" id="log_box">
            <property name="blockcursor">true</property>
            <property name="borderwidth">1</property>
            <property name="height">10</property>
            <property name="insertontime">0</property>
            <property name="insertwidth">0</property>
            <property name="maxundo">0</property>
            <property name="padx">10</property>
            <property name="pady">9</property>
            <property name="relief">flat</property>
            <property name="selectborderwidth">0</property>
            <property name="width">100</property>
            <layout>
              <property name="column">0</property>
              <property name="padx">15</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Scrollbar" id="log_box_scrollbar">
            <property name="orient">vertical</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
              <property name="sticky">n</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="ttk.Frame" id="top_frame_left">
        <property name="height">400</property>
        <property name="width">400</property>
        <layout>
          <property name="column">0</property>
          <property name="columnspan">1</property>
          <property name="pady">15</property>
          <property name="propagate">True</property>
          <property name="row">1</property>
        </layout>
        <child>
          <object class="tk.Entry" id="wssurl">
            <property name="text" translatable="yes">enter your url (ws or wss)</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="tk.Button" id="connect_button">
            <property name="command">on_connect_clicked</property>
            <property name="default">disabled</property>
            <property name="justify">left</property>
            <property name="pady">0</property>
            <property name="text" translatable="yes">Connect</property>
            <bind add="" handler="" sequence="" />
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">4</property>
              <property name="sticky">e</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="tk.Label" id="Websocket URL">
            <property name="takefocus">false</property>
            <property name="text" translatable="yes">Websocket Server URL</property>
            <property name="underline">0</property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
              <property name="sticky">e</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="tk.Label" id="label_connection_status">
            <property name="text" translatable="yes">Current Connection Status</property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">2</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="tk.Label" id="connection_status">
            <property name="text" translatable="yes">not connected</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">2</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="ttk.Labelframe" id="frame_bottom_left">
        <property name="height">200</property>
        <property name="text" translatable="yes">Data to send</property>
        <property name="width">200</property>
        <layout>
          <property name="column">0</property>
          <property name="columnspan">3</property>
          <property name="propagate">True</property>
          <property name="row">5</property>
          <property name="sticky">w</property>
        </layout>
        <child>
          <object class="tk.Text" id="data_to_send">
            <property name="height">11</property>
            <property name="insertborderwidth">0</property>
            <property name="insertofftime">200</property>
            <property name="maxundo">1</property>
            <property name="selectborderwidth">1</property>
            <property name="tabstyle">wordprocessor</property>
            <property name="width">80</property>
            <layout>
              <property name="column">1</property>
              <property name="padx">15</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Button" id="send_button">
            <property name="command">on_send_button_clicked</property>
            <property name="state">disabled</property>
            <property name="text" translatable="yes">Send Data</property>
            <layout>
              <property name="column">1</property>
              <property name="padx">15</property>
              <property name="pady">15</property>
              <property name="propagate">True</property>
              <property name="row">2</property>
              <property name="sticky">w</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Labelframe" id="label_frame_pred_messages">
            <property name="height">200</property>
            <property name="text" translatable="yes">Predefined messages</property>
            <property name="width">200</property>
            <layout>
              <property name="column">2</property>
              <property name="propagate">True</property>
              <property name="row">1</property>
              <property name="sticky">n</property>
            </layout>
            <child>
              <object class="tk.Listbox" id="predefined_messages">
                <layout>
                  <property name="column">1</property>
                  <property name="propagate">True</property>
                  <property name="row">1</property>
                </layout>
              </object>
            </child>
            <child>
              <object class="ttk.Button" id="button_predefined_message">
                <property name="command">on_use_predefined_message_clicked</property>
                <property name="text" translatable="yes">Use message</property>
                <layout>
                  <property name="column">1</property>
                  <property name="propagate">True</property>
                  <property name="row">2</property>
                </layout>
              </object>
            </child>
          </object>
        </child>
      </object>
    </child>
    <child>
      <object class="ttk.Frame" id="top_frame_right">
        <property name="height">200</property>
        <property name="width">200</property>
        <layout>
          <property name="column">1</property>
          <property name="padx">15</property>
          <property name="pady">15</property>
          <property name="propagate">True</property>
          <property name="row">1</property>
          <property name="sticky">n</property>
        </layout>
        <child>
          <object class="ttk.Label" id="label_header">
            <property name="text" translatable="yes">Header</property>
            <layout>
              <property name="column">0</property>
              <property name="propagate">True</property>
              <property name="row">3</property>
              <property name="sticky">e</property>
            </layout>
          </object>
        </child>
        <child>
          <object class="ttk.Combobox" id="header">
            <property name="exportselection">true</property>
            <property name="values">None ocpp1.6 ocpp1.5</property>
            <layout>
              <property name="column">1</property>
              <property name="propagate">True</property>
              <property name="row">3</property>
            </layout>
          </object>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
