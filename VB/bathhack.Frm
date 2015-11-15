VERSION 4.00
Begin VB.Form Form1 
   Caption         =   "intel Edison"
   ClientHeight    =   5010
   ClientLeft      =   4110
   ClientTop       =   1740
   ClientWidth     =   6690
   Height          =   5415
   Left            =   4050
   LinkTopic       =   "Form1"
   ScaleHeight     =   5010
   ScaleWidth      =   6690
   Top             =   1395
   Width           =   6810
   Begin VB.CommandButton Command2 
      Caption         =   "Congradulate!"
      Height          =   615
      Left            =   1920
      TabIndex        =   4
      Top             =   1920
      Width           =   1935
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Do Magic!"
      Height          =   615
      Left            =   1920
      TabIndex        =   3
      Top             =   1200
      Width           =   1935
   End
   Begin VB.CommandButton btnTransmit 
      Caption         =   "Transmit"
      Height          =   375
      Left            =   5400
      TabIndex        =   2
      Top             =   360
      Width           =   1095
   End
   Begin VB.TextBox txtMorse 
      Height          =   375
      Left            =   1800
      TabIndex        =   1
      Text            =   "SOS"
      Top             =   360
      Width           =   3495
   End
   Begin AgentObjectsCtl.Agent Agent1 
      Left            =   120
      Top             =   1920
      _cx             =   
      _cy             =   
   End
   Begin MSCommLib.MSComm MSComm1 
      Left            =   120
      Top             =   1200
      _Version        =   65536
      _ExtentX        =   847
      _ExtentY        =   847
      _StockProps     =   0
      CDTimeout       =   0
      CommPort        =   1
      CTSTimeout      =   0
      DSRTimeout      =   0
      DTREnable       =   -1  'True
      Handshaking     =   0
      InBufferSize    =   1024
      InputLen        =   0
      Interval        =   1000
      NullDiscard     =   0   'False
      OutBufferSize   =   512
      ParityReplace   =   "?"
      RThreshold      =   0
      RTSEnable       =   0   'False
      Settings        =   "9600,n,8,1"
      SThreshold      =   0
   End
   Begin VB.Label Label1 
      Caption         =   "Message to send:"
      Height          =   375
      Left            =   120
      TabIndex        =   0
      Top             =   360
      Width           =   1575
   End
End
Attribute VB_Name = "Form1"
Attribute VB_Creatable = False
Attribute VB_Exposed = False



Private Sub btnTransmit_Click()
    MSComm1.Output = txtMorse.Text
    Agent1.Characters("Merlin").Speak txtMorse.Text
End Sub

Private Sub Command1_Click()
    Agent1.Characters("Merlin").Play "DoMagic1"
End Sub


Private Sub Command2_Click()
    Agent1.Characters("Merlin").Play "Congradulate"
End Sub

Private Sub Form_Load()
    MSComm1.PortOpen = True
    Agent1.Characters.Load "Merlin"
    Agent1.Characters("Merlin").Show
End Sub


Private Sub Timer1_Timer()
    Text = MSComm1.Input + " "
    Agent1.Characters("Merlin").Speak Text
    MSComm1.Output = vbCrLf
    
End Sub


