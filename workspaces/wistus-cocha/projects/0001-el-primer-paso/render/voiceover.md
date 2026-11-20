---
project: "0001-el-primer-paso"
workspace: "wistus-cocha"
type: "audio_voiceover"
language: "es-BO"
voice_profile: "Locutor masculino boliviano de tono grave, épico, solemne, con textura cálida y dicción impecable (inspirador, místico y enérgico, estilo documental cinematográfico o spot Nike / Beast Mode)."
tempo_sync: "125 BPM"
recommended_tools: ["ElevenLabs", "Google Text-to-Speech", "PlayHT", "CapCut AI Voice", "Locución Humana en Estudio"]
---

# 🎙️ GUIA DE VOZ EN OFF (VOICEOVER & LOCUCIÓN)
**Proyecto:** Tráiler de Expectativa / Convocatoria: El Primer Paso (`0001-el-primer-paso`)  
**Workspace:** Tinkus Wistus - Filial Cochabamba (`wistus-cocha`)  

---

## 1. PARÁMETROS TÉCNICOS PARA GENERACIÓN (ELEVENLABS / TTS)

* **Voice Settings (ElevenLabs):**
  * **Stability:** 40% - 50% (Permite mayor expresividad e inflexión dramática).
  * **Clarity + Similarity:** 85% (Dicción limpia sobre la pista de bombos y charangos).
  * **Style Exaggeration:** 15% - 25% (Añade gravedad y epicidad sin sonar teatral fingido).
* **Idioma & Acento:** Español Latinoamericano con fonética boliviana natural (énfasis en fuerza consonántica andina, sin modismos extranjeros).
* **Mezcla Sonora:** 
  * La voz debe ubicarse al centro en el master final.
  * Sidechain compression / ducking leve sobre `render/music.md` para que la percusión no tape la voz.

---

## 2. GUION DE LOCUCIÓN: OPCIÓN CONVOCATORIA ("VIVE LA EXPERIENCIA WISTUS")
*Optimizada para el montaje híbrido (Tomas 1-4 con Mateo + Footage Real de Tropa + Toma 5 Ensayos).*

| Tiempo | Escena Visual / Tomas | Texto de Locución (Español) | Dirección de Inflexión y Tono |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:03.5** | **Tomas 1 y 2 (Mateo):**<br/>Zapateo macro 120fps, polvo y ajuste de abarca. | *«Muchos ven la fiesta desde afuera...»* | Tono íntimo, grave, reflexivo y susurrado pero con peso. Pausa dramática al final. |
| **0:03.5 - 0:07.5** | **Tomas 3 y 4 (Mateo):**<br/>Espalda bordada y postura marcial de combate Tinku. | *«...pocos sienten el llamado de hacer temblar la tierra.»* | Inflexión ascendente, voz profunda que proyecta poder y desafío interior. |
| **0:07.5 - 0:11.5** | **Metraje Real (Tropa):**<br/>Explosión de zapateo en multitud, polvo y euforia colectiva. | *«Llegó tu momento de sentir la fuerza de la tropa.»* | Explosión de energía, convicción rotunda, ritmo acelerado y vibrante. |
| **0:11.5 - 0:16.0** | **Toma 5 (Endcard Oficial):**<br/>Logo oficial Cochabamba + Placa de Ensayos. | *«Vive la experiencia WISTUS. Ensayos Filial Cochabamba. ¡Te esperamos!»* | Cálido, convocante, orgulloso y con llamado directo a la acción. |

---

## 3. GUION DE LOCUCIÓN: OPCIÓN TEASER PURO (13 SEGUNDOS)
*Optimizada para el corte original de expectativa con cierre "MUY PRONTO".*

| Tiempo | Escena Visual / Tomas | Texto de Locución (Español) | Dirección de Inflexión y Tono |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:03** | **Tomas 1 y 2 (Mateo):**<br/>Zapateo en asfalto y preparación. | *«El valle empieza a retumbar...»* | Susurro tenso y solemne. |
| **0:03 - 0:07** | **Toma 3 (Mateo):**<br/>Chaquetilla bordada y montera. | *«La armadura despierta.»* | Firmeza militar andina. |
| **0:07 - 0:10** | **Toma 4 (Mateo):**<br/>Zancada marcial y puñetazo al frente. | *«Cochabamba... el gigante vuelve a pisar fuerte.»* | Clímax vocal, rotundo y épico. |
| **0:10 - 0:13** | **Toma 5 (Endcard):**<br/>Logo oficial y destellos. | *«Tinkus Wistus. Muy pronto.»* | Tono misterioso y conclusivo. |

---

## 4. PROMPT PROMPT LISTO PARA ELEVENLABS / TEXT-TO-SPEECH

```text
[Tone: deep, solemn, cinematic documentary narrator, Andean epic warrior style, resonant low pitch, controlled breathing, powerful cadence synchronized at 125 BPM]

Muchos ven la fiesta desde afuera... [pause 0.5s] 
pocos sienten el llamado de hacer temblar la tierra. [pause 0.5s] 
Llegó tu momento de sentir la fuerza de la tropa. [energetic rise] 
Vive la experiencia WISTUS. Ensayos Filial Cochabamba. ¡Te esperamos!
```
