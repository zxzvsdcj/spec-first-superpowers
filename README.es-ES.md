# Especificación primero + Superpoderes v5

[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Compatible con Cursor](https://img.shields.io/badge/Cursor-Compatible-brightgreen)](https://cursor.sh)
[![Predeterminado: OpenSpec](https://img.shields.io/badge/Predeterminado-OpenSpec_OPSX-blue)](https://github.com/Fission-AI/OpenSpec)

Una habilidad de Cursor Agent que garantiza un flujo de trabajo basado en especificaciones antes de la codificación. Evita que la IA omita el diseño y pase directamente a la implementación.

## Instalación

```bash
npx skills add zxzvsdcj/spec-first-superpowers
```

Instalación no interactiva (para scripts/CI):

```bash
npx skills add zxzvsdcj/spec-first-superpowers --skill spec-first-superpowers --agent cursor --global --yes
```

Verificar la instalación:

```bash
npx skills ls -g -a cursor
```

> El comando de instalación sigue la convención de [vercel-labs/skills](https://github.com/vercel-labs/skills).

## Habilidades dependientes

Estas deben instalarse a través del marketplace de habilidades de Cursor o mediante `npx skills add`:

- `using-superpowers` + sub-habilidades (brainstorming, planes de escritura, TDD, revisión de código, etc.)
- `planning-with-files`
- `ui-ux-pro-max` (recomendado, v2.5.0)
- `finishing-a-development-branch`

Herramientas externas opcionales:

- **MemPalace** (`pip install mempalace`) — memoria entre sesiones y grafo de conocimiento.

Scripts de ayuda para herramientas CLI externas:

```bash
# Linux / macOS
chmod +x install-all.sh && ./install-all.sh
```

```powershell
# Windows PowerShell
.\install-all.ps1
```

## Uso

En cualquier chat de Cursor:

```
/super-spec
```

| Comando | Efecto |
|---------|--------|
| `/super-spec` | Flujo de trabajo completo (modo automático + complejidad automática) |
| `/super-spec force-spec-kit` | Forzar modo Spec-Kit |
| `/super-spec force-openspec` | Forzar modo OpenSpec |
| `/super-spec reset` | Restablecer selección de modo |
| `/super-spec upgrade` | Verificar actualizaciones en todos los proyectos integrados y ejecutar la actualización |

## Cómo funciona

```
/super-spec → Selección de modo → Triaje de complejidad → Recuperación de sesión (automática + MemPalace)
/    → Especificación (G1, con revisión de especificaciones en línea)
/    → Planificación persistente (G2, con revisión de planes en línea + mapeo de estructura de archivos)
/    → Diseño UI/UX (G3, condicional, sistema de diseño inteligente v2.5.0)
/    → Implementación TDD (G4, con selección de modelo + estado del implementador)
/    → Archivo (+ persistencia de MemPalace)
```

## Novedades de la versión 5

- **Autorevisión en línea**: Reemplazamos los bucles de revisión de subagentes con listas de verificación en línea rápidas (~30 segundos frente a ~25 minutos, calidad comparable, a partir de Superpowers v5.0.6).
- **Integración de MemPalace**: Memoria entre sesiones con un 96,6 % de recuperación R@5, grafo de conocimiento para el seguimiento de decisiones y diario del agente para la auditoría del flujo de trabajo.
- **Motor de flujo de trabajo Spec-Kit**: Registro y descubrimiento de flujos de trabajo personalizados a través del sistema de catálogo (v0.7.0+).
- **OpenSpec `/opsx:refine`**: Revisión y refinamiento específicos de artefactos (perfil personalizado).
- **Cambio de nombre del perfil OpenSpec**: "expanded" → "custom" (v1.2.0).
- **ui-ux-pro-max v2.5.0**: +6 habilidades especializadas (diseño de banners, diapositivas, estilo UI, sistema de diseño, diseño, marca), pila Three.js, base de datos de 1923 fuentes de Google.
- **Referencias de versiones actualizadas**: Spec-Kit v0.7.1, OpenSpec v1.2.0, Superpowers v5.0.7, planning-with-files v2.30.0.

### Características heredadas de la versión 4

- Triaje de complejidad (rápido/estándar/minucioso)
- Recuperación de sesión con prueba de reinicio de 5 preguntas
- Puertas de calidad G0-G4 con verificación de constitución
- Revisión en dos etapas (conformidad de especificaciones + calidad del código)
- Ejecución impulsada por subagentes sin contaminación de contexto
- Escalada de errores: Protocolo de 3 strikes + depuración sistemática
- Persistencia del diseño: `--persist` para reutilización entre sesiones
- Mapeo de estructura de archivos antes de la descomposición de tareas
- Selección de modelo para ejecución de subagentes (rápido → estándar → capaz)
- Manejo del estado del implementador (DONE/DONE_WITH_CONCERNS/NEEDS_CONTEXT/BLOCKED)
- Verificación del alcance para detección temprana de descomposición
- 6 cadenas de sinergia (actualizadas con la cadena MemPalace)

## Estructura del proyecto

```
spec-first-superpowers/
├── skills/
│   └── spec-first-superpowers/             # ← npx skills add instala solo este directorio
│       ├── SKILL.md                        # Lógica de orquestación principal (v5)
│       ├── references/
│       │   ├── spec-kit-workflow.md
│       │   ├── openspec-workflow.md
│       │   ├── integration-guide.md
│       │   ├── quality-gates.md
│       │   ├── synergy-patterns.md
│       │   ├── mempalace-integration.md    # Nuevo en v5
│       │   └── upgrade-protocol.md        # Nuevo en v5 — /super-spec upgrade
│       └── assets/
│           └── constitutions/
│               ├── openspec-constitution.md
│               └── spec-kit-constitution.md
├── .cursor/
│   └── 00-spec-first-superpowers.mdc       # Regla de guardia siempre activa
├── test_skill.py                           # Script de validación
├── install-all.sh / install-all.ps1        # Scripts de instalación de ayuda
└── README.md
```

> `npx skills add` detecta el subdirectorio `skills/` e instala solo su contenido. Los archivos de desarrollo en la raíz del repositorio no están incluidos.

## Proyectos integrados

| Proyecto | GitHub | Versión | Función |
|---------|--------|---------|------|
| Spec-Kit | [github/spec-kit](https://github.com/github/spec-kit) | v0.7.1 | Marco de trabajo impulsado por especificaciones de GitHub (instalación con uv tool) |
| OpenSpec | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | v1.2.0 | Flujo de trabajo OPSX ligero (predeterminado, npm) |
| Superpowers | [obra/superpowers](https://github.com/obra/superpowers) | v5.0.7 | Metodología TDD + revisión en línea + subagentes |
| planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | v2.30.0 | Planificación persistente basada en archivos |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | v2.5.0 | Sistema de diseño UI/UX |
| MemPalace | [MemPalace/mempalace](https://github.com/MemPalace/mempalace) | v3.3.0 | Memoria entre sesiones y grafo de conocimiento (opcional) |

---

Hades @Hades96444367 · Singapur · 2026
