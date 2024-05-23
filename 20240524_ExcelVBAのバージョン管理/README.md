## Excel VBA をテキストファイルとして保存する方法
初心者向け
新人教育
Excel
VBA

Excel VBA（えくせる　ぶいびーえー）は Microsoft Excel の機能を拡張し、自動化するためのプログラミング言語です。
VBA はマクロとも呼ばれ、セルやシートのデータ操作を自動化する事ができます。
ここでは 18 歳の新入社員向けに Excel VBA をテキストファイルとして保存する方法を紹介します。

## Excel VBA をテキストファイルとして保存する目的
通常 VBA のソースコードは、Excel ファイル（.xlsm）の中に埋め込まれており、Excel　の Visual Basic Editor（VBE）を使って内容を確認・編集することができます。
VBA をテキストファイルとして保存すると、以下のような利点が得られます。

### ソースコードの再利用
同じ動作を複数のワークブックやプロジェクトで再利用したい場合に、処理を簡単に移植することができます。

### バージョン管理
テキストファイルで扱う事で、Gitなどのバージョン管理システムとの連携が容易になります。

### ドキュメンテーション
コードをテキストファイルとして保存することで、ドキュメント化が容易になります。

### Excel VBA をテキストファイルとして保存する方法

以下の VBA コードを実行することで、現在のワークブック内のすべてのVBAコードが指定したフォルダにテキストファイルとして保存されます。

``` VB
' Copyright © 2024 Takatoshi Yamaoka
' 
' This code is licensed under the MIT License
' 
' Permission is hereby granted, free of charge, to any person obtaining a copy
' of this software and associated documentation files (the "Software"), to deal
' in the Software without restriction, including without limitation the rights
' to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
' copies of the Software, and to permit persons to whom the Software is
' furnished to do so, subject to the following conditions:
' 
' The above copyright notice and this permission notice shall be included in all
' copies or substantial portions of the Software.
' 
' THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
' IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
' FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
' AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
' LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
' OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
' SOFTWARE.
Option Explicit

Sub SaveAllVBA()
    Dim vbaComponent As Object
    Dim fileName As String
    Dim filePath As String
    Dim exportFolder As String
    Dim vbProj As Object
    
    ' 保存フォルダを設定
    exportFolder = ThisWorkbook.Path & "\VBA_Export\"
    
    ' 保存フォルダが存在しない場合、フォルダを作成する
    If Dir(exportFolder, vbDirectory) = "" Then
        MkDir exportFolder
    End If
    
    ' ファイルに含まれる VBA　コンポーネントのループ処理
    Set vbProj = ThisWorkbook.VBProject
    For Each vbaComponent In vbProj.VBComponents
        ' 各コンポーネントの名前と拡張子を名前を設定する
        Select Case vbaComponent.Type
            Case 1 ' 標準モジュール
                fileName = vbaComponent.Name & ".bas"
            Case 2 ' クラスモジュール
                fileName = vbaComponent.Name & ".cls"
            Case 3 ' ユーザーフォーム
                fileName = vbaComponent.Name & ".frm"
            Case 100 ' ワークシートまたはワークブック
                fileName = vbaComponent.Name & ".cls"
            Case Else
                fileName = vbaComponent.Name & ".txt"
        End Select
        filePath = exportFolder & fileName
        
        ' VBAコンポーネントをテキストファイルとして保存する
        vbaComponent.Export filePath
    Next vbaComponent
    
    MsgBox "All VBA code has been exported to " & exportFolder
End Sub
```

### 動作の説明
VBA コードが行う処理は以下の通りです。

#### 保存フォルダの設定
VBAコードを保存するフォルダを指定します。ここでは、現在のワークブックのフォルダに「VBA_Export」というフォルダを作成します。
#### フォルダの作成
MkDirを使って、指定したフォルダが存在しない場合は新しく作成します。
#### VBAコンポーネントのループ処理
VBProjectオブジェクトを使って、ワークブック内のすべてのVBAコンポーネント（標準モジュール、クラスモジュール、シートモジュール、フォーム）をループ処理します。
#### ファイル名の設定
各コンポーネントの名前と種類に基づいて、適切なファイル拡張子を付けたファイル名を設定します。
#### エクスポート
Exportメソッドを使って、各VBAコンポーネントをテキストファイルとして保存します。
#### 完了メッセージ
処理が完了したことを知らせるメッセージボックスを表示します。

### テキストファイルをExcel VBA のソースコードとして読込む方法

以下の VBA コードを実行すると、指定したフォルダ内の全ての VBA コードファイルが現在のワークブックにインポートされます。

``` VB
' Copyright © 2024 Takatoshi Yamaoka
' 
' This code is licensed under the MIT License
' 
' Permission is hereby granted, free of charge, to any person obtaining a copy
' of this software and associated documentation files (the "Software"), to deal
' in the Software without restriction, including without limitation the rights
' to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
' copies of the Software, and to permit persons to whom the Software is
' furnished to do so, subject to the following conditions:
' 
' The above copyright notice and this permission notice shall be included in all
' copies or substantial portions of the Software.
' 
' THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
' IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
' FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
' AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
' LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
' OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
' SOFTWARE.
Option Explicit

Sub ImportAllVBA()
    Dim vbaComponent As Object
    Dim fileName As String
    Dim filePath As String
    Dim importFolder As String
    Dim fileExtension As String
    Dim fileList As Variant
    Dim file As Variant
    
    ' インポートフォルダを設定
    importFolder = ThisWorkbook.Path & "\VBA_Export\"
    
    ' フォルダの存在を確認
    If Dir(importFolder, vbDirectory) = "" Then
        MsgBox "Import folder does not exist.", vbCritical
        Exit Sub
    End If
    
    ' ファイルリストの取得
    fileList = Application.FileDialog(msoFileDialogFilePicker)
    With fileList
        .InitialFileName = importFolder & "*.bas;*.cls;*.frm"
        .AllowMultiSelect = True
        .Title = "Select files to import"
        .Filters.Clear
        .Filters.Add "VBA Files", "*.bas;*.cls;*.frm", 1
        If .Show = -1 Then
            For Each file In .SelectedItems
                ' ファイル拡張子の取得
                fileExtension = Right(file, Len(file) - InStrRev(file, "."))
                
                ' ファイルのインポート
                Select Case fileExtension
                    Case "bas", "cls", "frm"
                        ThisWorkbook.VBProject.VBComponents.Import file
                    Case Else
                        MsgBox "Skipping unknown file type: " & file, vbExclamation
                End Select
            Next file
        Else
            MsgBox "No files selected.", vbExclamation
        End If
    End With
    
    MsgBox "All selected VBA code files have been imported."
End Sub
```

### 動作の説明
VBA コードが行う処理は以下の通りです。

#### インポートフォルダの設定
 インポートするVBAコードファイルが格納されているフォルダを指定します。ここでは、現在のワークブックのフォルダに「VBA_Export」というフォルダを想定しています。

#### フォルダの存在を確認
Dir関数を使用して、指定したフォルダが存在するかどうかを確認します。

#### ファイルダイアログの設定
Application.FileDialogオブジェクトを使用して、ユーザーがインポートするファイルを選択できるようにします。

#### ファイルリストの取得
選択されたファイルのリストを取得し、ループで各ファイルを処理します。

#### ファイル拡張子の取得
Right関数とInStrRev関数を使って、ファイルの拡張子を取得します。

#### ファイルのインポート
VBComponents.Importメソッドを使用して、各ファイルをインポートします。

#### 完了メッセージ
処理が完了したことを知らせるメッセージボックスを表示します。
