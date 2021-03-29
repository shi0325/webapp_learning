onload = function() {
    draw();
  };
   
  function draw() {
    var canvas = document.getElementById('rectangle');
    if ( ! canvas || ! canvas.getContext ) {
      return false;
    }
    var cvs = canvas.getContext('2d');
   
    /* rectangle */
    cvs.strokeRect(0,0,600,600); // (50,50)の位置に100x100のサイズの四角形を描く
    cvs.strokeRect(0,0,600,20)
    cvs.strokeRect(100,400,400,200)
    cvs.strokeRect(200,500,200,100)

    cvs.strokeStyle = 'black';  // 線の色
    // パスの開始
    cvs.beginPath();
    cvs.arc(300, 20, 80, 0, 2 * Math.PI, false);
    // 描画
    cvs.stroke();

    let name = document.getElementById('player_name').value;
    let names = name.slice(0,-1).split(',');

    var num_of_GK = 1;
    let num_of_DF = Number(document.getElementById('df').value);
    let num_of_MF = Number(document.getElementById('mf').value);
    let num_of_FW = Number(document.getElementById('fw').value);

    var y = 70;
    var i = 0;

    for (let name of names) {
        name = name.slice(2,-1)
        cvs.font = "12px 'ＭＳ ゴシック'";
        var metrics = cvs.measureText(name);
        var textWidth = metrics.width;
        if (num_of_FW == i || num_of_FW+num_of_MF == i || num_of_FW+num_of_MF+num_of_DF == i){
            y = y + 170;
        }
        // fwの配置
        if (i < num_of_FW){
            if (num_of_FW >= 3){
                st = 80
                x = (600 - st*2) / (num_of_FW-1);
                if (num_of_FW == 5 && i == 2){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW - i-1), y-20);
                    i = i + 1;
                    continue;
                }
                if (i == 0 || i == num_of_FW-1){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW - i-1), y+20);
                    i = i + 1;
                    continue;
                }
                else{
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW - i-1), y);
                    i = i + 1;
                    continue;
                }
            }
            x = 600 / (num_of_FW+1);
            cvs.fillText(name, (x-(textWidth/2))+x*(num_of_FW - i-1), y);
        }
        // mfの配置
        else if ( num_of_FW<=i && i<(num_of_FW+num_of_MF) ){
            if (num_of_MF > 3){
                st = 80
                x = (600 - st*2) / (num_of_MF-1);
                if (num_of_MF == 5 && i-num_of_FW == 2){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF-i-1), y+60);
                    i = i + 1;
                    continue;
                }
                if (i == num_of_FW || i == num_of_FW + num_of_MF-1){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF-i-1), y-20);
                    i = i + 1;
                    continue;
                }
                else{
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF-i-1), y+40);
                    i = i + 1;
                    continue;
                }
            }
            x = 600 / (num_of_MF+1);
            cvs.fillText(name, (x-(textWidth/2))+x*(num_of_FW+num_of_MF-i-1), y+40);
        }
        // dfの配置
        else if ((num_of_FW+num_of_MF)<=i && i<(num_of_FW+num_of_MF+num_of_DF)){
            if (num_of_DF > 3){
                st = 80;
                x = (600 - st*2) / (num_of_DF-1);
                if (num_of_FW == 5 && i-num_of_FW-num_of_MF == 2){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF+num_of_DF-i-1), y+40);
                    i = i + 1;
                    continue;
                }
                if (i == num_of_FW+num_of_MF || i == num_of_FW + num_of_MF + num_of_DF-1){
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF+num_of_DF-i-1), y-20);
                    i = i + 1;
                    continue;
                }
                else{
                    cvs.fillText(name, (st-(textWidth/2))+x*(num_of_FW+num_of_MF+num_of_DF-i-1), y+20);
                    i = i + 1;
                    continue;
                }
            }
            x = 600 / (num_of_DF+1);
            cvs.fillText(name, (x-(textWidth/2))+x*(num_of_FW+num_of_MF+num_of_DF-i-1), y+20);
        }
        // gkの配置
        else{
            x = 600 / (num_of_GK+1);
            cvs.fillText(name, (x-(textWidth/2)), y);
        }
        i = i + 1;
      }  
}

