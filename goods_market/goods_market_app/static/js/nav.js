$('body').prepend(`    
    <!-- Панель навигации -->
    <nav class="navbar navbar-expand-xl navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">
            <!-- <img src="./img/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="not found" loading="lazy"> -->
            <i class="fa-solid fa-seedling" style="color: #0efb35;"></i>
            <!-- <i class="fa-solid fa-gamepad fa-sm" style="color: #0efb35;"></i> -->
            Продукты 24
        </a>

        <!-- Кнопка бургер -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarWithDropdown" aria-controls="navbarWithDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarWithDropdown">
            <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Главная</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Доставка</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Категории
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                    <li><a class="dropdown-item" href="#">Свежие овощи и фрукты</a></li>
                    <li><a class="dropdown-item" href="#">Молочная продукция</a></li>
                    <li><a class="dropdown-item" href="#">Мясо</a></li>
                </ul>
            </li>
            </ul>
        </div>
    </div>
    </nav>
`);