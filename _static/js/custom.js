const clName = document.getElementsByClassName;

if (clName('.rst-content img').style.height >= '150px')
{
    clName('.rst-content img').style.width = 'auto';
}
else
{
    clName('.rst-content img').style.width = '100%';
}