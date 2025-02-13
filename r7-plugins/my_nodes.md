[Пример пути до установленного пользовательского плагина](C:\Users\User\AppData\Local\R7-Office\Editors\data\sdkjs-plugins\{FFE1F462-1EA2-4391-990D-4CC84940B754})

[How to set a value to a file input in HTML to a client side disk file system path?](https://stackoverflow.com/questions/1696877/how-to-set-a-value-to-a-file-input-in-html-to-a-client-side-disk-file-system-pat)


[Плагин для Р7 'Вложенные файлы'](https://nct.r7-office.ru/api/v1/link?uid=ba59b886-ff07-4028-9935-17d566f6edc3_341327&download=true)

```javascript
(function (window, undefined) {
    window.Asc.plugin.init = function () {
        console.log(window["AscDesktopEditor"]["SaveQuestion"]());
        console.log(this);
        documentFilePath = parent.AscDesktopEditor.LocalFileGetSourcePath();
        console.log(documentFilePath)

        fs.createReadStream(filePath);
        // .pipe(request.put(putURL,options,function(err, httpsResponse, body){
        //     if ( err ) {
        //         console.log('err', err);
        //     } else {
        //         console.log(body);
        //     }
        // }));


        // var sh=Api.GetSheets();
        // console.log(sh);
        // console.log(Api.GetFullName());
        // this.callCommand(function() {
        //     // var oDocument = Api.GetDocument();
        //     // console.log(oDocument);

        // //     var oParagraph = Api.CreateParagraph();
        // //     oParagraph.AddText("Hello world!");
        // //     oDocument.InsertContent([oParagraph]);
        // }, true);
    };
    window.Asc.plugin.button = function (id) {
        console.log(id)
        this.executeCommand("close", '');
    };
```