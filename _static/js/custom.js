const SelAll = document.querySelectorAll;

if (SelAll('.rst-content img').style.height >= '150px')
{
    SelAll('.rst-content img').style.width = 'auto';
}
else
{
    SelAll('.rst-content img').style.width = '100%';
}