document.addEventListener('DOMContentLoaded', function() {
  const slides = document.querySelectorAll('.carousel-slide');
  const track = document.querySelector('.carousel-track');
  let currentSlide = 0;
  const slideCount = slides.length;
  const slideWidth = 1200; // 与图片宽度相同

  function showSlide(index) {
    // 计算需要滚动的距离
    const offset = -index * slideWidth;
    track.style.transform = `translateX(${offset}px)`;
  }

  // 初始显示第一张图片
  showSlide(currentSlide);

  // 可以添加按钮或自动播放逻辑来切换图片
  // 例如，添加自动播放功能
  setInterval(() => {
    currentSlide = (currentSlide + 1) % slideCount;
    showSlide(currentSlide);
  }, 3000); // 每3秒切换一次图片
});
// 获取轮播轨道元素
const carouselTrack = document.querySelector('.carousel-track');
// 图片索引，初始为0
let currentIndex = 0;
// 图片数量
const slideCount = carouselTrack.children.length;
// 轮播间隔时间（单位：毫秒）
const intervalTime = 2000; 
// 用于存储定时器的变量
let timer;

function nextSlide() {
    currentIndex++;
    if (currentIndex >= slideCount) {
        currentIndex = 0;
    }
    const slideWidth = carouselTrack.children[0].offsetWidth;
    const offset = -currentIndex * slideWidth;
    carouselTrack.style.transform = `translateX(${offset}px)`;
}

function startCarousel() {
    timer = setInterval(nextSlide, intervalTime);
}

function stopCarousel() {
    clearInterval(timer);
}

// 页面加载完成后启动轮播
window.onload = function () {
    startCarousel();
};
