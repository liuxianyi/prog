/* 命名空间、参数 */
var fire = {
    c: document.createElement('canvas'),
    particles: [], // 粒子集合
    particleCount: 300, // 粒子总数
    particlePath: 4, // 拖尾长度
    pillars: [], // 圆集合
    pillarCount: 30, // 圆总数
    hue: 0, // 颜色偏移参数，色调
    hueRange: 60, // 颜色偏移范围
    hueChange: 1, // 颜色渐变步长
    gravity: 0.06, // 重力
    lineWidth: 2, // 划线宽度
    lineCap: 'round', // 线条样式
    pillarSize: 30, // 圆尺寸
    PI: Math.PI,
    TWO_PI: Math.PI * 2,
    particleRadius: 3, // 粒子半径
    select: $("#canvas"), // 选择器，容器，整个浏览器界面
    pillarAlive: 0, // 圆存活总数
    particleAlive: 0, // 存活粒子总数
    colorful: false, // 色彩模式
    staticColor: 'rgba(20, 20, 40, 0.3)' // 圆初始颜色
};

/* 初始配置，修改：全屏显示 */
fire.config = function (width, height) {
    fire.ctx = fire.c.getContext('2d');
    fire.w = fire.c.width = width; // 画布宽度
    fire.h = fire.c.height = height; // 画布高度
}

/* 生成随机数 */
fire.rand = function (min, max) {
    return Math.random() * (max - min) + min;
}

/* 两点间距 */
fire.distance = function (a, b) {
    var dx = a.x - b.x,
        dy = a.y - b.y;
    return Math.sqrt(dx * dx + dy * dy);
}

/* 生成随机颜色 */
fire.getColor = function () {
    if (fire.colorful) {
        return "rgba(" + ~~fire.rand(0, 255) + ", " + ~~fire.rand(0, 255) + ", " + ~~fire.rand(0, 255) + ", 0.3)"
    } else {
        return fire.staticColor;
    }
}

/* 粒子类 */
fire.Particle = function (opt) {
    this.path = []; // 拖尾
    this.reset(); // 初始化
}

/* 初始化粒子属性 */
fire.Particle.prototype.reset = function () {
    this.radius = fire.particleRadius; // 粒子半径
    this.x = fire.rand(0, fire.w); // 随机从0-x出生
    this.y = 0; // 初始y坐标为0
    this.vx = 0; // 横向速度
    this.vy = 0; // 纵向速度
    this.hit = 0; // 碰撞状态
    this.path.length = 0; // 无拖尾
    if (fire.particleAlive > fire.particleCount) {
        fire.particles.pop(); // 删除一个
        fire.particleAlive--;
    }
};

/* 粒子每一步的动作*/
fire.Particle.prototype.step = function () {
    this.hit = 0;
    this.path.unshift([this.x, this.y]);
    if (this.path.length > fire.particlePath) { // 当前粒子拖尾长度大于设定上限
        this.path.pop(); // 清除尾部拖尾
    }
    this.vy += fire.gravity; // 纵向加速度
    this.x += this.vx; // 横向位移
    this.y += this.vy; // 纵向位移

    // 越界检验
    if (this.y > fire.h + 10) { // 纵向越界
        this.reset();
    } else if (this.x > fire.w + 10 || this.x < -10) { // 横向越界
        this.reset();
    }

    // 碰撞检测：粒子与圆
    var i = fire.pillarCount;
    while (i--) { // 遍历圆
        var pillar = fire.pillars[i];
        if (pillar && fire.distance(this, pillar) < this.radius + pillar.renderRadius) { // 当前粒子与当前圆发生碰撞
            // 根据位置生成反弹速度
            this.vx = -(pillar.x - this.x) * fire.rand(0.01, 0.03);
            this.vy = -(pillar.y - this.y) * fire.rand(0.01, 0.03);
            pillar.radius -= 0.5; // 圆的形式半径下降
            this.hit = 1; // 碰撞状态中
        }
    }
};

/* 粒子绘制方法 */
fire.Particle.prototype.draw = function () {
    fire.ctx.beginPath();
    fire.ctx.moveTo(this.x, ~~this.y); // 移动到粒子当前位置
    for (var i = 0, length = this.path.length; i < length; i++) { // 创建粒子拖尾路径
        var point = this.path[i];
        fire.ctx.lineTo(point[0], ~~point[1]);
    }
    // 设置颜色、绘制路径，色调、饱和度、亮度、不透明度
    fire.ctx.strokeStyle = 'hsla(' + fire.rand(fire.hue + (this.x / 3), fire.hue + (this.x / 3) + fire.hueRange) + ', 50%, 30%, 0.3)'; // 划线颜色
    fire.ctx.stroke(); // 划线

    // 碰撞状态发光
    if (this.hit) {
        fire.ctx.beginPath();
        fire.ctx.arc(this.x, this.y, fire.rand(1, 25), 0, fire.TWO_PI); // 粒子当前位置创建圆形路径
        fire.ctx.fillStyle = 'hsla(' + fire.rand(fire.hue + (this.x / 3), fire.hue + (this.x / 3) + fire.hueRange) + ', 80%, 15%, 0.1)' // 填充颜色
        fire.ctx.fill(); // 填充
    }
};

/* 圆类 */
fire.Pillar = function (x, y) {
    this.reset(x, y); // 初始化
}

/* 初始化方法 */
fire.Pillar.prototype.reset = function (xx, yy) {
    this.radius = fire.rand(fire.pillarSize, fire.pillarSize * 2); // 形式半径
    this.renderRadius = 0; // 真实半径
    if (xx && yy) {
        // 在指定的坐标处生成
        this.x = xx;
        this.y = yy;
        fire.pillarAlive++;
        fire.pillarCount++;
    } else {
        this.x = fire.rand(0, fire.w); // 生成x坐标
        this.y = fire.rand(fire.h / 4, fire.h); // 生成y坐标，下3/4位置
    }
    this.active = 0; // 真实半径达到形式半径，处于激活状态，未激活则真实半径一直增加
    this.color = fire.getColor();
};

/* 每步动作 */
fire.Pillar.prototype.step = function () {
    if (this.active) { // 处于激活状态
        if (this.radius <= 3) { // 形式半径太小
            this.reset(); // 重置
        } else { // 形式半径与真实半径同步
            this.renderRadius = this.radius;
        }
    } else { // 未激活状态
        if (this.renderRadius < this.radius) { // 真实半径持续增加
            this.renderRadius += 0.2;
        } else { // 增加结束，激活
            this.active = 1;
        }
    }
};

/* 越界检验，只在重设窗口时使用 */
fire.Pillar.prototype.check = function () {
    if (this.x > fire.w || this.y > fire.h) {
        this.reset();
    }
}

/* 圆绘制方法 */
fire.Pillar.prototype.draw = function () {
    fire.ctx.beginPath();
    fire.ctx.arc(this.x, this.y, this.renderRadius, 0, fire.TWO_PI, false); // 当前位置创建圆路径
    fire.ctx.fillStyle = this.color;
    fire.ctx.fill(); // 填充
};

/* 全局初始化方法 */
fire.init = function () {
    // 使用画布宽度进行初始化
    fire.config(fire.select.width(), fire.select.height());
    fire.ctx.lineWidth = fire.lineWidth;
    fire.ctx.lineCap = fire.lineCap;

    fire.select.append(fire.c);
    fire.loop();
}

/* 执行所有对象的每步动作 */
fire.step = function () {
    fire.hue += fire.hueChange; // 颜色渐变
    
    // 圆数量检测
    if (fire.pillarAlive > fire.pillarCount) {
        fire.pillars.pop(); // 从集合中清除一个
        fire.pillarAlive--;
    }

    // 插入新粒子
    if (fire.particleAlive < fire.particleCount) {
        fire.particles.push(new fire.Particle());
        fire.particleAlive++;
    }

    // 创建圆
    if (fire.pillarAlive < fire.pillarCount) {
        fire.pillars.push(new fire.Pillar());
        fire.pillarAlive++;
    }

    // 执行每个粒子动作
    var i = fire.particles.length;
    while (i--) {
        fire.particles[i].step();
    }

    // 执行每个圆动作
    i = fire.pillarCount;
    while (i-- && fire.pillars[i]) {
        fire.pillars[i].step();
    }
}

/* 绘制所有对象 */
fire.draw = function () {
    // 背景黑色
    fire.ctx.fillStyle = 'hsla(0, 0%, 0%, 0.1)';
    fire.ctx.fillRect(0, 0, fire.w, fire.h);

    // 图像重叠时拼合图像，包括颜色和形状
    fire.ctx.globalCompositeOperation = 'lighter';
    var i = fire.particles.length;
    while (i--) { // 绘制所有粒子
        fire.particles[i].draw();
    }

    // 覆盖图层下的图像
    fire.ctx.globalCompositeOperation = 'source-over';
    i = fire.pillarCount; // 圆颜色
    fire.ctx.fillStyle = 'rgba(20, 20, 40, 0.3)';
    while (i-- && fire.pillars[i]) { // 绘制所有圆
        fire.pillars[i].draw();
    }
}

/* 主循环 */
fire.loop = function () {
    // 动画，优化资源占用
    requestAnimationFrame(fire.loop);
    fire.step();
    fire.draw();
}

/* 开始动画 */
fire.init();

/* 改变粒子数量，回调函数用于提示，错误时调用，返回出错信息 */
fire.changeParticleCount = function (count, fn) {
    if (count > 1000) {
        fn("粒子数量太多");
    } else if (count <= 0) {
        fn("粒子数量太少");
    } else if (count) {
        fire.particleCount = count;
    } else {
        fn("非法数值");
    }
}

/* 改变圆数量，回调函数用于提示，错误时调用，返回出错信息 */
fire.changePillarCount = function (count, fn) {
    if (count > 100) {
        fn("圆数量太多");
    } else if (count <= 0) {
        fn("圆数量太少");
    } else if (count) {
        fire.pillarCount = count;
    } else {
        fn("非法数值");
    }
}

/* 改变颜色与颜色模式 */
fire.changeColor = function (mode, color) {
    if (mode) {
        fire.colorful = true;
    } else {
        fire.colorful = false;
        fire.staticColor = color;
    }
    var i = fire.pillarCount;
    while (i--) {
        fire.pillars[i].color = fire.getColor()
    }
}

/* 窗口大小改变则重设，修改：全屏显示 */
window.addEventListener("resize", function () {
    // 使用画布宽度进行重设
    var i = fire.pillarCount;
    fire.config(fire.select.width(), fire.select.height());
    while (i--) { // 对每个圆补充越界检验
        fire.pillars[i].check();
    }
})

/* 点击事件监听 */
window.addEventListener("click", function (event) {
    // 新元素应该在的位置
    var newX = event.clientX - fire.select[0].getBoundingClientRect().left;
    var newY = event.clientY - fire.select[0].getBoundingClientRect().top;
    if (newX < fire.w && newX > 0 && newY < fire.h && newY > 0) {
        if (fire.pillarCount >= 100) {
            alert("无法创建更多");
            return;
        }
        fire.pillars.push(new fire.Pillar(newX, newY));
    }
})