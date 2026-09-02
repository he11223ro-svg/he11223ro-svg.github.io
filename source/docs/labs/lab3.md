# Отчет по лабораторной работе №3
**Тема:** CI/CD для статического сайта в SourceCraft и GitHub Actions
**Выполнил:** Альшухайед Рами

---

## 1. Цель работы
Реализовать сценарий автоматического развертывания статического сайта, построенного на движке **MkDocs**, с использованием платформ **GitHub Actions** и **SourceCraft**.

---

## 2. Выполненные шаги

### Настройка SourceCraft
1. Авторизовался на `sourcecraft.dev` через аккаунт Яндекс.
2. Создал публичную организацию `alshuhayed` и пустой репозиторий `he11223ro-svg-github-io`.
3. Создал Personal Access Token (PAT) с правами `Maintainer`.
4. Добавил второй remote-репозиторий в локальный проект:
```bash
git remote add sourcecraft https://alshuhayed:<TOKEN>@git.sourcecraft.dev/alshuhayed/he11223ro-svg-github-io.git